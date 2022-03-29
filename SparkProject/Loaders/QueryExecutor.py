import time


class QueryExecutor:
    def __init__(self, database, catalog, output_location):
        self.database = database
        self.catalog = catalog
        self.output_location = output_location

    def execute(self, connector, query):
        try:
            q1 = connector.get_connection().start_query_execution(
                QueryString=query,
                QueryExecutionContext={
                    'Database': self.database,
                    'Catalog': self.catalog
                },
                ResultConfiguration={
                    'OutputLocation': self.output_location
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
