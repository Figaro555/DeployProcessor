from Transformers.YouTube.ChannelTransformer import ChannelTransformer


class ChannelFrameCreator():
    def __init__(self):
        self.channel_trans = ChannelTransformer()

    def create_df(self, spark_session, data):
        channel_data = data.map(lambda channel: self.channel_trans.transform_to_tuple(channel))
        df = spark_session.createDataFrame(channel_data, ["id", "title", "video_count", "view_count", "description",
                                                          "subscriber_count"])
        df.printSchema()
        df.show(truncate=False)
        return df
