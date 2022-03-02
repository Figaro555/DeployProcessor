from DataGetters.AbstractDataGetter import AbstractDataGetter


class ChannelDataGetter(AbstractDataGetter):
    def get_data(self, channels_id, connector):
        result = []
        
        for channel_id in channels_id:
            c_response = None
            
            while c_response is None:
                try:
                    c_request =(connector.get_connection()).channels().list(
                        part='statistics, snippet, contentDetails',
                        id=channel_id
                    )
                    c_response = c_request.execute()
                    result += [c_response]
                
                except Exception as _ex:
                    c_response = None
                    connector.index += 1
                    if connector.index >= connector.api_arr_len:
                        return result
        return result
        