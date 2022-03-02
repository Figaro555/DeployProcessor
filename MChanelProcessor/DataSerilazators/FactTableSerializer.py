from DataSerilazators.AbstractDataSerializator import AbstractDataSerializator
from Entities.Video import Video


class FactTableSerializer(AbstractDataSerializator):
    def serialize(self, video: Video, date_id, channel_id):
        return {"video_id": video.video_id, "channel_id": channel_id, "date_id": date_id,
                "view_count": int(video.view_count), "like_count": int(video.like_count),
                "hour": int(video.hour), "comment_count": int(video.comments)}
