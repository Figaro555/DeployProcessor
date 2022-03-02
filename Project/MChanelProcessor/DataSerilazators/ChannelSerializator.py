from DataSerilazators.AbstractDataSerializator import AbstractDataSerializator
from Entities.Channel import Channel


class ChannelSerializator(AbstractDataSerializator):
    def serialize(self, channel: Channel):
        return {"id": channel.channel_id, "title": channel.title, "video_count": int(channel.video_count),
                "view_count": int(channel.view_count), "description": channel.description,
                "subscriber_count": int(channel.subscriber_count)}
