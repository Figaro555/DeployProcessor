from pyspark import SparkContext

from Connectors.AthenaConnector import AthenaConnector
from Loaders.Aggregation.QueryCreator.LastChannelViews import LastChannelViews
from Loaders.Aggregation.QueryCreator.TopChannelSub import TopChannelSub
from Loaders.Aggregation.QueryCreator.TopVideoComment import TopVideoComment
from Loaders.Aggregation.QueryCreator.TopVideoLiked import TopVideoLiked
from Loaders.ClearData.AthenaDataManager import AthenaDataManager
from Loaders.QueryExecutor import QueryExecutor
from channel_ids import my_channels_id
from Extractors.YouTube.ChannelDataExtractor import ChannelDataExtractor
from Extractors.YouTube.VideoDataExtractor import VideoDataExtractor
from Connectors.YouTubeConnector import YouTubeConnector
from Transformers.YouTubeTransformer import YouTubeTransformer

from datetime import datetime
import time


def main():
    sc = SparkContext("local[*]")
    sc.setLogLevel("ERROR")

    cd = ChannelDataExtractor()
    vd = VideoDataExtractor()
    transformer = YouTubeTransformer()
    clear_data_loader = AthenaDataManager()

    t = datetime.now()
    hour = str(t.hour)
    date = str(datetime.date(t))
    time1 = str(datetime.fromtimestamp(int(time.time())))

    executor = QueryExecutor('mdatabasea', 'AwsDataCatalog', 's3://mbucket111111/Athena/queryResults/')

    print(date)
    print(datetime)

    channels_id_rdd = sc.parallelize(my_channels_id)

    channels = channels_id_rdd.map(lambda channel: cd.get_data(channel, YouTubeConnector()))

    channels_with_videos = channels.map(
        lambda channel: vd.get_data(channel,
                                    YouTubeConnector()))

    entities = channels_with_videos.map(lambda channel: transformer.transform_to_local_array(channel, hour))

    clear_data = entities.map(lambda channel: clear_data_loader.process_data(channel, date))

    clear_data.count()
    executor.execute(AthenaConnector(), "MSCK REPAIR TABLE `fact1`;")

    queries = sc.parallelize([TopVideoComment().create_query(time1, date, hour),
                              TopVideoLiked().create_query(time1, date, hour),
                              TopChannelSub().create_query(time1, date, hour),
                              LastChannelViews().create_query(time1, date, hour)])

    agg = queries.map(lambda query: executor.execute(AthenaConnector(), query))

    executor.execute(AthenaConnector(), "MSCK REPAIR TABLE `channelagg1`;")
    executor.execute(AthenaConnector(), "MSCK REPAIR TABLE `videoagg1`;")

    print(agg.collect())


if __name__ == '__main__':
    main()
