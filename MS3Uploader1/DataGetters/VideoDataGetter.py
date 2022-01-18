from DataGetters.AbstractDataGetter import AbstractDataGetter


class VideoDataGetter(AbstractDataGetter):
    def get_data(self, playlist_id, connector):
        pl_request = (connector.get_connection()).playlistItems().list(
            part='contentDetails',
            playlistId=playlist_id,
            maxResults=50
        )
        pl_response = pl_request.execute()

        return [(connector.get_connection()).videos().list(
            part='statistics, snippet',
            id=item["contentDetails"]["videoId"]
        ).execute() for item in pl_response["items"]]
