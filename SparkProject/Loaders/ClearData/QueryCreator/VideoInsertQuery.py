from Entities.Video import Video


class VideoInsertQuery:
    def create_query(self, video: Video):
        return "INSERT INTO video1 (id, title) \n" + \
               "VALUES ('" + video.video_id + "', '" + video.title + "')"
