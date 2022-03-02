from DataGetters.AbstractDataGetter import AbstractDataGetter


class VideoDataGetter(AbstractDataGetter):
    def get_data(self, playlist_id, connector):
        pl_response = None
        
        while pl_response is None:
            try:
                pl_request = (connector.get_connection()).playlistItems().list(
                    part='contentDetails',
                    playlistId=playlist_id,
                    maxResults=50
                )
                pl_response = pl_request.execute()
                
            except Exception as _ex:
                pl_response = None
                connector.index += 1
                if connector.index >= connector.api_arr_len:
                    return []
        
        
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
                        return result
        return result
