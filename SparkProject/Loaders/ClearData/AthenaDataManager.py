from Connectors.AthenaConnector import AthenaConnector
from Loaders.ClearData.QueryCreator.ChannelInsertQuery import ChannelInsertQuery
from Loaders.ClearData.QueryCreator.DateInsertQuery import DateInsertQuery
from Loaders.ClearData.QueryCreator.FactInsertQuery import FactInsertQuery
from Loaders.ClearData.QueryCreator.VideoInsertQuery import VideoInsertQuery
from Loaders.QueryExecutor import QueryExecutor


class AthenaDataManager:

    def process_data(self, channel, date_id):
        cquery = ChannelInsertQuery()
        dquery = DateInsertQuery()
        fquery = FactInsertQuery()
        vquery = VideoInsertQuery()

        connector = AthenaConnector()
        executor = QueryExecutor('mdatabasea', 'AwsDataCatalog', 's3://mbucket111111/Athena/queryResults/')

        date = date_id.split("-")
        executor.execute(connector, cquery.create_query(channel))

        executor.execute(connector, dquery.create_query(date_id, date[2], date[1], date[0]))

        for video in channel.videos:
            executor.execute(connector, fquery.create_query(video, date_id, channel.channel_id))
            executor.execute(connector, vquery.create_query(video))

