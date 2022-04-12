from pyspark.sql import DataFrame, SparkSession

from DataFrameProcessors.Aggregation.DataFrameQueryExecutor import DataFrameQueryExecutor
from DataFrameProcessors.queries import queries


class DataFrameAggregator():
    def __init__(self, spark_session: SparkSession, path_to_save):
        self.executor = DataFrameQueryExecutor()
        self.spark_session = spark_session
        self.path_to_save = path_to_save

    def agregate(self, fact_table: DataFrame, video_table: DataFrame, channel_table: DataFrame, date, hour):

        video_and_fact = video_table.join(fact_table, video_table['id'] == fact_table['video_id'], 'left')

        self.aggregate_last_channel_view(channel_table, date, hour)
        self.aggregate_top_channel_subscribers(channel_table, date, hour)
        self.aggregate_top_video_comment(video_and_fact)
        self.aggregate_top_video_liked(video_and_fact)

    def aggregate_last_channel_view(self, channel_table, date, hour):
        self.executor.run_query(channel_table, queries["LastChannelView"].format(date, hour), self.spark_session). \
            write.mode('append').partitionBy('date_id',
                                             'hour',
                                             'category') \
            .json(self.path_to_save + "/Aggregated")

    def aggregate_top_channel_subscribers(self, channel_table, date, hour):
        self.executor.run_query(channel_table, queries["TopChannelSubscribers"].format(date, hour), self.spark_session) \
            .write.mode('append').partitionBy('date_id',
                                              'hour',
                                              'category') \
            .json(self.path_to_save + "/Aggregated")

    def aggregate_top_video_comment(self, video_and_fact):
        self.executor.run_query(video_and_fact, queries["TopVideoComment"], self.spark_session). \
            write.mode('append').partitionBy('date_id',
                                             'hour',
                                             'category') \
            .json(self.path_to_save + "/Aggregated")

    def aggregate_top_video_liked(self, video_and_fact):
        self.executor.run_query(video_and_fact, queries["TopVideoLiked"], self.spark_session) \
            .write.mode('append').partitionBy('date_id',
                                              'hour',
                                              'category') \
            .json(self.path_to_save + "/Aggregated")
