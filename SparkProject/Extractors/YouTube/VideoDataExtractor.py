from Extractors.YouTube.AbstractDataExtractor import AbstractDataExtractor


class VideoDataExtractor(AbstractDataExtractor):

    def get_video_ids(self, channel, connector):
        playlist_id = channel["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

        pl_response = None

        while pl_response is None:
            try:
                pl_request = (connector.get_connection()).playlistItems().list(
                    part='contentDetails',
                    playlistId=playlist_id,
                    maxResults=2
                )
                pl_response = pl_request.execute()

            except Exception as _ex:
                pl_response = None
                connector.index += 1
                if connector.index >= connector.api_arr_len:
                    raise Exception('Keys are expired')

        return pl_response

    def get_data(self, channel, connector):

        pl_response = self.get_video_ids(channel, connector)

        result = []

        for item in pl_response["items"]:
            v_response = None

            while v_response is None:
                try:
                    v_request = (connector.get_connection()).videos().list(
                        part='statistics, snippet',
                        id=item["contentDetails"]["videoId"]
                    )
                    v_response = v_request.execute()
                    result += [v_response]

                except Exception as _ex:
                    v_response = None
                    connector.index += 1
                    if connector.index >= connector.api_arr_len:
                        raise Exception('Keys are expired')
        channel["videos"] = result
        return channel
