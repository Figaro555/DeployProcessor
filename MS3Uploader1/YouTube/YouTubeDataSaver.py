import json

from YouTube.YouTubeConnector import YouTubeConnector
from DataGetters.ChannelDataGetter import ChannelDataGetter
from DataGetters.VideoDataGetter import VideoDataGetter


class YouTubeDataLoader():
    def __init__(self, my_channels_id):
        self.channel_getter = ChannelDataGetter()
        self.video_getter = VideoDataGetter()
        self.connector = YouTubeConnector()
        self.channel_ids = my_channels_id

    def save(self):
        channels = self.channel_getter.get_data(self.channel_ids, self.connector)

        for channel in channels:
            channel["videos"] = self.video_getter.get_data(
                channel["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"],
                self.connector)

        result_json = {"root": channels}

        return result_json
