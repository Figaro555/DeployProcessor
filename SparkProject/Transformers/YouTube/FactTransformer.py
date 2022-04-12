from Transformers.AbstractTransformer import AbstractTransformer


class FactTransformer(AbstractTransformer):
    video_id = ""
    channel_id = ""
    view_count = 0
    like_count = 0
    comment_count = 0

    def transform_to_tuple(self, video, hour, date_id):
        try:
            video_id = video["items"][0]["id"]
        except Exception as _ex:
            video_id = 0

        try:
            channel_id = video["items"][0]["snippet"]["channelId"]
        except Exception as _ex:
            channel_id = ""

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

        return (
            video_id.replace("'", "''"), channel_id.replace("'", "''"), view_count, like_count, comments, date_id,
            hour)
