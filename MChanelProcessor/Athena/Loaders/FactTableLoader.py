import json
from collections import defaultdict

import boto3
from Athena.Loaders.AbstractLoader import AbstractLoader


class FactLoader(AbstractLoader):
    def load(self, facts, bucket_name, part):
        s3 = boto3.resource('s3')
        dd = defaultdict(lambda: defaultdict(list))

        for v in facts:
            dd[v["hour"]][v["date_id"]].append(v)
        
        
        for hour in dd.keys():
            for date in dd[hour].keys():
                with open("/tmp/" +str(date) + str(hour) + "data.json", "w") as f:
                    for i, fact in enumerate(dd[hour][date]):
                        s = json.dumps(fact)
                        f.write(s)
                        if i != len(facts) - 1:
                            f.write(",")
                        f.write("\n")
            s3.meta.client.upload_file("/tmp/" + str(date) + str(hour) + 'data.json', bucket_name,
                                       'Athena/src/Fact/date_id=' + date + '/hour=' + str(hour) + '/data' + str(part) + '.json')
