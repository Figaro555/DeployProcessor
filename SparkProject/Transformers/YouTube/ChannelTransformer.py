from Entities.Channel import Channel
from Transformers.AbstractTransformer import AbstractTransformer


class ChannelTransformer(AbstractTransformer):
    channel_id = "0"
    channel_title = ""
    videoCount = 0
    viewCount = 0
    subscriber_count = 0
    description = ""
    videos = None

    def transform_to_local_array(self, channel, hour):
        try:
            channel_id = channel["items"][0]["id"]
        except Exception as _ex:
            channel_id = ""

        try:
            channel_title = channel["items"][0]["snippet"]["title"]
        except Exception as _ex:
            channel_title = ""

        try:
            videoCount = int(channel["items"][0]["statistics"]["videoCount"])
        except Exception as _ex:
            videoCount = 0

        try:
            viewCount = int(channel["items"][0]["statistics"]["viewCount"])
        except Exception as _ex:
            viewCount = 0

        try:
            if channel["items"][0]["statistics"]["hiddenSubscriberCount"] == True:
                subscriber_count = 0
            subscriber_count = int(channel["items"][0]["statistics"]["subscriberCount"])
        except Exception as _ex:
            subscriber_count = 0

        try:
            description = channel["items"][0]["snippet"]["description"]
        except Exception as _ex:
            description = ""

        return Channel(channel_id, channel_title, viewCount, videoCount, description, subscriber_count, None)