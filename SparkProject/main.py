from datetime import datetime

from pyspark.sql import SparkSession

from Executor.Executor import Executor


def main():
    path_to_save = '/home/admin1/Рабочий стол/SparkProject1/test'
    start_time = datetime.now()
    ss = SparkSession.builder.master("local[*]").getOrCreate()
    executor = Executor()
    executor.execute(ss, path_to_save)
    print(datetime.now() - start_time)


if __name__ == '__main__':
    main()
