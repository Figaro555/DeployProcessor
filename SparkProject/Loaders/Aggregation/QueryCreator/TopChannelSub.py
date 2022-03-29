class TopChannelSub:
    def create_query(self, time1, date_id, hour):
        return "Insert into mdatabasea.channelagg1 (id, title, view_count, subscriber_count , time, category, date_id, hour) " + \
               "select distinct c.id, c.title, Max(c.video_count) as video_count, Max(c.subscriber_count) as subscriber_count, " + \
               "cast('" + time1 + "' as timestamp) , 'Top Channel Subscribers','" + date_id + "'," + str(hour) + " " + \
               "from mdatabasea.channel1 as c group by c.title, c.id order by subscriber_count desc limit 3;"
