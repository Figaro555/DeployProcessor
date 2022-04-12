from datetime import datetime

from Connectors.YouTubeConnector import YouTubeConnector
from Extractors.YouTube.ChannelDataExtractor import ChannelDataExtractor
from Extractors.YouTube.VideoDataExtractor import VideoDataExtractor
from Extractors.channel_ids import my_channels_id


class Executor:

    def execute(self, ss):
        ss.sparkContext.setLogLevel("ERROR")

        cd = ChannelDataExtractor()
        vd = VideoDataExtractor()

        channels_id_rdd = ss.sparkContext.parallelize(my_channels_id)

        channels = channels_id_rdd.map(lambda channel: cd.get_data(channel, YouTubeConnector()))

        videos = channels.flatMap(lambda channel: vd.get_data(channel,
                                                              YouTubeConnector()))

