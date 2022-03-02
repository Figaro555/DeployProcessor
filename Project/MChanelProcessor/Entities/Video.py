class Video:
    def __eq__(self, o: object) -> bool:
        if isinstance(o, Video):
            return (self.video_id == o.video_id and
                    self.title == o.title and
                    self.like_count == o.like_count and
                    self.view_count == o.view_count)


        return False

    def __init__(self, video_id, title, like_count, view_count, hour, comments):
        self.video_id = video_id
        self.title = title
        self.like_count = like_count
        self.view_count = view_count
        self.hour = hour
        self.comments = comments
