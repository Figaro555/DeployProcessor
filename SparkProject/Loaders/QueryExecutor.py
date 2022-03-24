import time


class QueryExecutor:
    def execute(self, connector, query):
        try:
            q1 = connector.get_connection().start_query_execution(
                QueryString=query,
                QueryExecutionContext={
                    'Database': 'mdatabasea',
                    'Catalog': 'AwsDataCatalog'
                },
                ResultConfiguration={
                    'OutputLocation': 's3://mbucket111111/Athena/queryResults/'
                }
            )

            q = q1['QueryExecutionId']
            status = connector.get_connection().get_query_execution(QueryExecutionId=q)['QueryExecution']['Status']['State']
            status_types = ['QUEUED', 'RUNNING']
            while status in status_types:
                if status in ['FAILED', 'CANCELLED']:
                    raise Exception("queue failed" + query)

                time.sleep(1)
                status = connector.get_connection().get_query_execution(QueryExecutionId=q)['QueryExecution']['Status']['State']
        except Exception as _ex:
            print(_ex)
            raise Exception("query failed: " + query)

        return query
