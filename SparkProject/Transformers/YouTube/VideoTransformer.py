from Entities.Video import Video
from Transformers.AbstractTransformer import AbstractTransformer


class VideoTransformer(AbstractTransformer):
    id = ""
    title = ""
    like_count = 0
    view_count = 0
    comments = 0

    def transform_to_local_array(self, video, hour):
        try:
            id = video["items"][0]["id"]
        except Exception as _ex:
            id = 0

        try:
            title = video["items"][0]["snippet"]["title"]
        except Exception as _ex:
            title = ""

        try:
            like_count = int(video["items"][0]["statistics"]["likeCount"])
        except Exception as _ex:
            like_count = 0

        try:
            view_count = int(video["items"][0]["statistics"]["viewCount"])
        except Exception as _ex:
            view_count = 0

        try:
            comments = int(video["items"][0]["statistics"]["commentCount"])
        except Exception as _ex:
            comments = 0

        return Video(id, title, like_count, view_count, hour, comments)
