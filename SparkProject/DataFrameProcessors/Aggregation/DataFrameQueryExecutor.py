from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import current_timestamp


class DataFrameQueryExecutor:

    def run_query(self, data_frame: DataFrame, query: str, spark_session: SparkSession):
        data_frame.createOrReplaceTempView("tmp")
        data = spark_session.sql(query).withColumn("time", current_timestamp())
        data.show()
        data.printSchema()
        return data
