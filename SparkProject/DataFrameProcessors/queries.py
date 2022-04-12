queries = {
    "TopVideoComment": '''SELECT t.id, t.title, t.like_count, t.comment_count, t.date_id, t.hour, 'TopVideoComment' as category FROM tmp as t order by t.comment_count desc  limit 3''',
    "TopVideoLiked": '''SELECT t.id, t.title, t.like_count, t.comment_count, t.date_id, t.hour, 'TopVideoLiked' as category FROM tmp as t order by t.like_count desc  limit 3''',
    "LastChannelView": '''SELECT t.id, t.title, t.video_count,t.view_count, t_subscriber_count, '{}'  as date_id, {} as hour, 'LastChannelView' as category FROM tmp as t order by t.view_count limit 3''',
    "TopChannelSubscribers": '''SELECT t.id, t.title, t.video_count,t.view_count, t_subscriber_count, '{}'  as date_id, {} as hour, 'TopChannelSubscribers' as category  FROM tmp as t order by t.subscriber_count desc limit 3'''
}
