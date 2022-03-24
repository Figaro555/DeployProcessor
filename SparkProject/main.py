import time
from datetime import datetime

from pyspark import SparkContext

from Connectors.AthenaConnector import AthenaConnector
from Connectors.YouTubeConnector import YouTubeConnector
from Extractors.YouTube.ChannelDataExtractor import ChannelDataExtractor
from Extractors.YouTube.VideoDataExtractor import VideoDataExtractor
from Loaders.ClearData.AthenaDataManager import AthenaDataManager
from Loaders.QueryExecutor import QueryExecutor
from Transformers.YouTubeTransformer import YouTubeTransformer
from channel_ids import my_channels_id


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

    executor = QueryExecutor()

    channels_id_rdd = sc.parallelize(my_channels_id)

    channels = channels_id_rdd.map(lambda channel: cd.get_data(channel, YouTubeConnector()))

    channels_with_videos = channels.map(
        lambda channel: vd.get_data(channel,
                                    YouTubeConnector()))

    entities = channels_with_videos.map(lambda channel: transformer.transform_to_local_array(channel, hour))

    clear_data = entities.map(lambda channel: clear_data_loader.process_data(channel, date))

    clear_data.count()
    executor.execute(AthenaConnector(), "MSCK REPAIR TABLE `fact1`;")


if __name__ == '__main__':
    main()
