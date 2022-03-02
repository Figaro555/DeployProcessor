import json
from YouTube.YouTubeDataSaver import YouTubeDataLoader

import boto3

def lambda_handler(event, context):
    
    bucket_name = "mbucket111111"
    massage_dict = event
    
    ytl = YouTubeDataLoader(massage_dict["array"])

    file_name = "/tmp/data"+ str(massage_dict["part"]) +".json"
    
    resource_path ="Resources/" + str(massage_dict["date"]) + "/" + str(massage_dict["hour"]) +  "/data" + str(massage_dict["part"]) + ".json"
    s3 = boto3.resource('s3')

    res = ytl.save()
    
    with open(file_name, 'w',  encoding='utf-8') as f:
        json.dump(res, f)
        
    
            
    s3.meta.client.upload_file(file_name, bucket_name, resource_path)
            
    return {
        'statusCode': 200,
        'body': {"file": resource_path, "time": massage_dict["time"]}
    }
