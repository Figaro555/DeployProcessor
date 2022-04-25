from datetime import datetime

from pyspark.sql import DataFrame

from Extractors.channel_ids import my_channels_id
from Connectors.YouTubeConnector import YouTubeConnector
from DataFrameProcessors.Aggregation.DataFrameAggregator import DataFrameAggregator
from DataFrameProcessors.DataFrameCreators.ChannelFrameCreator import ChannelFrameCreator
from DataFrameProcessors.DataFrameCreators.FactFrameCreator import FactFrameCreator
from DataFrameProcessors.DataFrameCreators.VideoFrameCreator import VideoFrameCreator
from Extractors.YouTube.ChannelDataExtractor import ChannelDataExtractor
from Extractors.YouTube.VideoDataExtractor import VideoDataExtractor


class Executor:

    def execute(self, ss, path_to_save):
        ss.sparkContext.setLogLevel("ERROR")

        cd = ChannelDataExtractor()
        vd = VideoDataExtractor()
        channel_df_cr = ChannelFrameCreator()
        video_df_cr = VideoFrameCreator()
        fact_df_cr = FactFrameCreator()
        aggregator = DataFrameAggregator(ss, path_to_save)

        t = datetime.now()
        hour = t.hour
        date = str(datetime.date(t))

        channels_id_rdd = ss.sparkContext.parallelize(my_channels_id)

        channels = channels_id_rdd.map(lambda channel: cd.get_data(channel, YouTubeConnector()))

        videos = channels.flatMap(lambda channel: vd.get_data(channel,
                                                              YouTubeConnector()))

        fact_table: DataFrame = fact_df_cr.create_df(ss, videos, date, hour)
        video_table: DataFrame = video_df_cr.create_df(ss, videos)
        channel_table: DataFrame = channel_df_cr.create_df(ss, channels)

        fact_table.write.mode('append').partitionBy("date_id", "hour").json(path_to_save + "/Fact")
        video_table.write.mode('append').json(path_to_save + "/Video")
        channel_table.write.mode('append').json(path_to_save + "/Channel")

        aggregator.agregate(fact_table, video_table, channel_table, date, hour)
