import json

import boto3
from Athena.Loaders.AbstractLoader import AbstractLoader


class ChannelLoader(AbstractLoader):
    def load(self, channels, bucket_name, part, date, hour):
        s3 = boto3.resource('s3')
        with open("/tmp/channel.json", "w", encoding="utf-8") as f:
            for i, channel in enumerate(channels):
                s = json.dumps(channel)
                f.write(s)
                if i != len(channels) - 1:
                    f.write(",")
                f.write("\n")
        s3.meta.client.upload_file('/tmp/channel.json', bucket_name, 'Athena/src/Channel/channel' + str(part) + "_" + date + "_" + str(hour) + '.json')
