from Transformers.AbstractTransformer import AbstractTransformer
from Transformers.YouTube.ChannelTransformer import ChannelTransformer
from Transformers.YouTube.VideoTransformer import VideoTransformer


class YouTubeTransformer(AbstractTransformer):

    def transform_to_local_array(self, channel, hour):

        channel_trans = ChannelTransformer()

        videos = []

        try:
            for video in channel["videos"]:
                video_trans = VideoTransformer()
                videos.append(video_trans.transform_to_local_array(video, hour))

        except Exception as _ex:
            videos = None

        res = channel_trans.transform_to_local_array(channel, hour)
        res.videos = videos

        return res
