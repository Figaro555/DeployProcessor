from pyspark.sql import DataFrame
from pyspark.sql.functions import current_timestamp, col, lit


class DataFrameProcessor:

    def process_data_frame(self, date_frame: DataFrame, columns_to_select: list, limit: int, column_to_compare: str,
                           desc: bool, category: str, hour, date):
        result = date_frame.select(*columns_to_select)
        result = result.sort(col(column_to_compare).desc()) if desc else result.sort(col(column_to_compare).asc())

        result = result.limit(limit) \
            .withColumn("date_id", lit(date)) \
            .withColumn("hour", lit(hour)) \
            .withColumn("category", lit(category)) \
            .withColumn("time", current_timestamp())

        result.show()

        return result
