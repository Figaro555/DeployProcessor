from time import time

import boto3 as boto3

from Config.YouTubeConfig import api_key


class AthenaConnector():
    def __init__(self):
        self.connection = None
        self.last_connection_update = 0.
        self.index = 0
        self.api_arr_len = len(api_key)

    def get_connection(self):
        if abs(time() - self.last_connection_update) > 3 * 60:
            self.last_connection_update = time()

            try:
                self.connection = boto3.client("athena")
                return self.connection

            except Exception as _ex:
                print("[ERROR] Error while creating connection with Athena", _ex)

        return self.connection
