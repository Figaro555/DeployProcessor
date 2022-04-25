from Transformers.YouTube.FactTransformer import FactTransformer


class FactFrameCreator():
    def __init__(self):
        self.fact_trans = FactTransformer()

    def create_df(self, spark_session, data, date, hour):
        fact_data = data.map(lambda video: self.fact_trans.transform_to_tuple(video, hour, date))
        df = spark_session.createDataFrame(fact_data, ["video_id", "channel_id", "view_count", "like_count",
                                                       "comment_count", "date_id",
                                                       "hour"])
        df.printSchema()
        df.show(truncate=False)

        return df
