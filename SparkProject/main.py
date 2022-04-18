import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from SparkProject.Executor.Executor import Executor


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])


sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

path_to_save = 's3://mbucket111111/Test'

executor = Executor()
executor.execute(spark, path_to_save)

job.commit()
