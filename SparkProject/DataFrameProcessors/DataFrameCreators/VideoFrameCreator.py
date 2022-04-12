from Transformers.YouTube.VideoTransformer import VideoTransformer


class VideoFrameCreator():
    def __init__(self):
        self.video_trans = VideoTransformer()

    def create_df(self, spark_session, data):
        video_data = data.map(lambda video: self.video_trans.transform_to_tuple(video))
        df = spark_session.createDataFrame(video_data, ["id", "title"])
        df.printSchema()
        df.show(truncate=False)

        return df
