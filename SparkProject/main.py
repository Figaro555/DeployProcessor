from datetime import datetime

from pyspark import SparkContext

from Connectors.YouTubeConnector import YouTubeConnector
from Extractors.YouTube.ChannelDataExtractor import ChannelDataExtractor
from Extractors.YouTube.VideoDataExtractor import VideoDataExtractor
from Transformers.YouTubeTransformer import YouTubeTransformer
from channel_ids import my_channels_id


def main():
    sc = SparkContext("local[*]")
    sc.setLogLevel("ERROR")

    cd = ChannelDataExtractor()
    vd = VideoDataExtractor()

    transformer = YouTubeTransformer()

    t = datetime.now()
    hour = str(t.hour)
    channels_id_rdd = sc.parallelize(my_channels_id)

    channels = channels_id_rdd.map(lambda channel: cd.get_data(channel, YouTubeConnector()))

    channels_with_videos = channels.map(
        lambda channel: vd.get_data(channel,
                                    YouTubeConnector()))

    entities = channels_with_videos.map(lambda channel: transformer.transform_to_local_array(channel, hour))

    print(entities.collect())


if __name__ == '__main__':
    main()
