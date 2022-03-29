from Extractors.YouTube.AbstractDataExtractor import AbstractDataExtractor


class ChannelDataExtractor(AbstractDataExtractor):

    def get_data(self, channel_id, connector):
        result = {}

        c_response = None

        while c_response is None:
            try:
                c_request = (connector.get_connection()).channels().list(
                    part='statistics, snippet, contentDetails',
                    id=channel_id
                )
                c_response = c_request.execute()
                return c_response

            except Exception as _ex:
                print(_ex)
                c_response = None
                connector.index += 1
                if connector.index >= connector.api_arr_len:
                    raise Exception('Keys are expired')
        return result
