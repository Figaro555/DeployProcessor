from Entities.Channel import Channel


class ChannelInsertQuery:
    def create_query(self, channel: Channel):
        return "INSERT INTO channel1 (id, title, video_count, view_count, description, subscriber_count)\n" + \
               "VALUES ('" + channel.channel_id + "', '" + channel.title + "'," + str(channel.view_count) + "," + \
               str(channel.video_count) + ", '" + channel.description + "', " + str(channel.subscriber_count) + ")"
