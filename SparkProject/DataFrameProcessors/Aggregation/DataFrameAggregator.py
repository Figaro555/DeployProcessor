from pyspark.sql import DataFrame, SparkSession

from DataFrameProcessors.Aggregation.DataFrameProcessor import DataFrameProcessor
from DataFrameProcessors.queries import query_data


class DataFrameAggregator():
    def __init__(self, spark_session: SparkSession, path_to_save):
        self.executor = DataFrameProcessor()
        self.spark_session = spark_session
        self.path_to_save = path_to_save

    def agregate(self, fact_table: DataFrame, video_table: DataFrame, channel_table: DataFrame, date, hour):
        video_and_fact = video_table.join(fact_table, video_table['id'] == fact_table['video_id'], 'left')
        partitions = ['date_id',
                      'hour',
                      'category']
        self.save_data_frame(
            self.process_aggregation(channel_table, date, hour, "LastChannelView"),
            partitions)

        self.save_data_frame(
            self.process_aggregation(channel_table, date, hour, "TopChannelSubscribers"),
            partitions)

        self.save_data_frame(
            self.process_aggregation(video_and_fact, date, hour, "TopVideoComment"),
            partitions)

        self.save_data_frame(
            self.process_aggregation(video_and_fact, date, hour, "TopVideoLiked"),
            partitions)

    def process_aggregation(self, data_frame, date, hour, category):
        return self.executor.process_data_frame(data_frame, query_data[category]["columns"],
                                                query_data[category]["count"],
                                                query_data[category]["column_to_compare"],
                                                query_data[category]["desc"], category, hour, date)

    def save_data_frame(self, data_frame: DataFrame, partitions: list):
        data_frame.write.mode('append').partitionBy(*partitions) \
            .json(self.path_to_save + "/Aggregated")