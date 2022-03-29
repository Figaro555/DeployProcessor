class Channel:

    def __init__(self, channel_id, title, video_count, view_count, description, subscriber_count,
                 videos):
        self.channel_id = channel_id
        self.title = title
        self.video_count = video_count
        self.view_count = view_count
        self.videos = videos
        self.description = description
        self.subscriber_count = subscriber_count
