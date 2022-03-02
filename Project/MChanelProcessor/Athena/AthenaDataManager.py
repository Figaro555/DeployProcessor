from DataSerilazators.ChannelSerializator import ChannelSerializator
from DataSerilazators.DateSerializator import DateSerializator
from DataSerilazators.FactTableSerializer import FactTableSerializer
from DataSerilazators.VideoSerializator import VideoSerializator
from Athena.Loaders.ChannelLoader import ChannelLoader
from Athena.Loaders.DateLoader import DateLoader
from Athena.Loaders.FactTableLoader import FactLoader
from Athena.Loaders.VideoLoader import VideoLoader


class AthenaDataManager:

    def process_data(self, data, date_id, bucket_name, part, hour):
        channel_serializator = ChannelSerializator()
        date_serializator = DateSerializator()
        video_serializator = VideoSerializator()
        fact_serializator = FactTableSerializer()
        
        date = date_id.split("-")
        
        date_json = date_serializator.serialize(date_id, date[2], date[1], date[0])
        
        channel_json = []
        video_json = []
        fact_json = []
        for channel in data:
            channel_json += [channel_serializator.serialize(channel)]
            for video in channel.videos:
                video_json += [video_serializator.serialize(video)]
                fact_json += [fact_serializator.serialize(video, date_json["id"], channel.channel_id)]

        channel_loader = ChannelLoader()
        video_loader = VideoLoader()
        date_loader = DateLoader()
        fact_loader = FactLoader()

        channel_loader.load(channel_json, bucket_name, part, date_id, hour)
        video_loader.load(video_json, bucket_name, part, date_id, hour)
        date_loader.load([date_json], bucket_name, part, date_id, hour)
        fact_loader.load(fact_json, bucket_name, part)
