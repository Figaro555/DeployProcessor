import json
import boto3
import math
import json
from YouTubeChannels import *
from datetime import datetime
import time


def lambda_handler(event, context):
    threads_num = 4
    n = math.ceil(len(my_channels_id)/threads_num)
    c = chunks(my_channels_id, n)
    t = datetime.now()
    l = list(range(0, threads_num))
    
    return {
        'statusCode': 200,
        'body': {"array": c, "hour": str(t.hour), "date": str(datetime.date(t)), "indexes": l, "time": str(datetime.fromtimestamp(int(time.time())))}
    }


def chunks(l, n):
    n = max(1, n)
    return [l[i:i+n] for i in range(0, len(l), n)]