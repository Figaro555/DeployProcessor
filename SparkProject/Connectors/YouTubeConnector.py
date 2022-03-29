from googleapiclient.discovery import build

from Config.YouTubeConfig import api_key
from Connectors.AbstractConnector import AbstractConnector


class YouTubeConnector(AbstractConnector):
    def create_connection(self):
        return build('youtube', 'v3', developerKey=api_key[self.index])

    def __init__(self):
        self.connection = None
        self.last_connection_update = 0.
        self.index = 0
        self.api_arr_len = len(api_key)
        self.type = "YouTube"
