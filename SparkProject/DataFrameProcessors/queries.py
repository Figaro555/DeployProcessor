query_data = {
    "LastChannelView": {
        "columns": ['id', 'title', 'video_count', 'view_count', 'subscriber_count'],
        "column_to_compare": 'view_count',
        "desc": False,
        "count": 3
    },
    "TopChannelSubscribers": {
        "columns": ['id', 'title', 'video_count', 'view_count', 'subscriber_count'],
        "column_to_compare": 'subscriber_count',
        "desc": True,
        "count": 3
    },
    "TopVideoComment": {
        "columns": ['id', 'title', 'like_count', 'comment_count'],
        "column_to_compare": 'comment_count',
        "desc": True,
        "count": 3
    },
    "TopVideoLiked": {
        "columns": ['id', 'title', 'like_count', 'comment_count'],
        "column_to_compare": 'like_count',
        "desc": True,
        "count": 3
    }

}