from DataGetters.AbstractDataGetter import AbstractDataGetter


class ChannelDataGetter(AbstractDataGetter):
    def get_data(self, channels_id, connector):
        return [(connector.get_connection()).channels().list(
            part='statistics, snippet, contentDetails',
            id=channel_id
        ).execute()
                for channel_id in channels_id]
