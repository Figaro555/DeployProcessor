from time import time

from googleapiclient.discovery import build

from Config.YouTubeConfig import api_key


class YouTubeConnector():
    def __init__(self):
        self.connection = None
        self.last_connection_update = 0.
        self.index = 0
        self.api_arr_len = len(api_key)

    def get_connection(self):
        if abs(time() - self.last_connection_update) > 3 * 60:
            self.last_connection_update = time()

            try:
                self.connection = build('youtube', 'v3', developerKey=api_key[self.index])
                return self.connection

            except Exception as _ex:
                print("[ERROR] Error while creating connection with YouTube API", _ex)

        return self.connection
