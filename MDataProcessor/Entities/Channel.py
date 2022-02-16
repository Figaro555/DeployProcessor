class Channel:

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Channel):
            return (self.channel_id == o.channel_id and
                    self.title == o.title and
                    self.view_count == o.view_count and
                    self.video_count == o.video_count and
                    self.hidden_subscriber_count == o.hidden_subscriber_count and
                    self.videos == o.videos)

        return False

    def __init__(self, channel_id, title, video_count, view_count, hidden_subscriber_count, description, videos):
        self.channel_id = channel_id
        self.title = title
        self.video_count = video_count
        self.view_count = view_count
        self.hidden_subscriber_count = hidden_subscriber_count
        self.videos = videos
        self.description = description
