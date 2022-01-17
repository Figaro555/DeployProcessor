import json
import boto3
import math
import json
from YouTubeChannels import *


def lambda_handler(event, context):
    threads_num = 5
    n = math.ceil(len(my_channels_id) / threads_num)
    c = chunks(my_channels_id, n)

    client = boto3.client("sqs")
    for i, ch in enumerate(c):
        client.send_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/062261762656/MSQSChannel',
            MessageBody=(json.dumps({"part": i, "array": ch}))
        )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


def chunks(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]
