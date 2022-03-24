class TopVideoLiked:
    def create_query(self, time1, date_id, hour):
        return "Insert into mdatabasea.videoagg1 (id, title, like_count, comment_count, time, category, date_id, hour)" + \
               " SELECT v.id, v.title, MAX(f.like_count) as like_count, MAX(f.comment_count) as comment_count, " + \
               "cast('" + time1 + "' as timestamp), 'Top Video Liked', '" + date_id + "', " + str(hour) + " " + \
               " FROM mdatabasea.fact1 as f" + \
               " Left JOIN mdatabasea.video1 as v ON v.id = f.video_id " + \
               "where f.date_id = '" + date_id + "' and f.hour = " + str(hour) + \
               " group by v.title, f.hour, f.date_id, v.id order by like_count desc limit 3;"

