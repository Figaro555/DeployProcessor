import boto3
import json

from Transformers.YouTubeTransformer import YouTubeTransformer
from Athena.AthenaDataManager import AthenaDataManager
from DataLoaders.S3DataLoader import S3DataLoader


def lambda_handler(event, context):
    bucket_name = "mbucket111111"
    
    changed_file_name = event["body"]["file"]
    part = int(((changed_file_name.split("/")[-1]).split(".")[0])[4:])
    print(part)
    
    date_id = changed_file_name.split("/")[-3]
    hour = changed_file_name.split("/")[-2]
    
    s3_loader = S3DataLoader()
    data = s3_loader.save(changed_file_name, bucket_name)
    
    yt_transformer = YouTubeTransformer()
    
    local_array = yt_transformer.transform_to_local_array(data["root"], hour)
    
    at_data_manager = AthenaDataManager()
    at_data_manager.process_data(local_array, date_id ,bucket_name, part, hour)

    return {
        'statusCode': 200,
        'body': {"date_id": date_id, "hour": hour, "time": event["body"]["time"]}
    }
