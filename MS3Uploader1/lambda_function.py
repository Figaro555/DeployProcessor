import json
from YouTube.YouTubeDataSaver import YouTubeDataLoader

import boto3

def lambda_handler(event, context):
    
    
    ytl = YouTubeDataLoader(event["array"])
    file_name = "/tmp/data"+ str(event["part"]) +".json"
    
    resource_path ="Resources/YouTubeData/data" + str(event["part"]) + ".json"
    
    s3 = boto3.resource('s3')
    bucket_name = "myprojectbucket111"
    
    
    with open(file_name, 'w') as f:
            json.dump(ytl.save(), f)
            
    s3.meta.client.upload_file(file_name, bucket_name, resource_path)
            
    return {
        'statusCode': 200,
        'body': event
    }
