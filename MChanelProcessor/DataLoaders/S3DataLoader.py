import os

import boto3
import json


class S3DataLoader:

    def save(self, file_name, bucket):
        s3 = boto3.client('s3')
        key = 'transactions.json'

        response = s3.get_object(Bucket=bucket, Key=file_name)

        content = response['Body']

        return json.loads(content.read())

