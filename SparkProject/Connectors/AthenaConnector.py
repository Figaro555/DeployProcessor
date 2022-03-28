import boto3 as boto3

from Connectors.AbstractConnector import AbstractConnector


class AthenaConnector(AbstractConnector):
    def create_connection(self):
        self.connection = boto3.client("athena")
        return self.connection

    def __init__(self):
        self.connection = None
        self.last_connection_update = 0.
        self.type = "Athena"
