from Entities.Video import Video


class FactInsertQuery:

    def create_query(self, video: Video, date_id, channel_id):
        return "INSERT INTO fact1 (video_id, channel_id, view_count, like_count, comment_count,date_id, hour)\n" + \
               "VALUES ('" + video.video_id + "', '" + channel_id + "'," + str(video.view_count) + \
               ", " + str(video.like_count) + ", " + str(video.comments) + ", '" + date_id + "'," + \
               str(video.hour) + " )"
