import json

import boto3
from Athena.Loaders.AbstractLoader import AbstractLoader


class DateLoader(AbstractLoader):
    def load(self, dates, bucket_name, part, date_1, hour):
        s3 = boto3.resource('s3')
        with open("/tmp/date.json", "w") as f:
            for i, date in enumerate(dates):
                s = json.dumps(date)
                f.write(s)
                if i != len(dates) - 1:
                    f.write(",")
                f.write("\n")
        s3.meta.client.upload_file('/tmp/date.json', bucket_name, 'Athena/src/Date/date' + str(part) + "_" + date_1 + "_" + str(hour)+ '.json')
