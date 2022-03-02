from Entities.Video import Video
from Entities.Channel import Channel
from Transformers.AbstractTransformer import AbstractTransformer


class YouTubeTransformer(AbstractTransformer):

    def transform_to_local_array(self, local_dl, hour):
        
        channels = []
        
        for channel in local_dl:
            channel_id = "0"
            channel_title = ""
            videoCount = 0
            viewCount = 0
            subscriber_count = 0
            description = ""
            videos = None
            
        
            try:
                channel_id = channel["items"][0]["id"] 
            except Exception as _ex:
                channel_id = 0
            
            try:
                channel_title = channel["items"][0]["snippet"]["title"]
            except Exception as _ex:
                channel_title = ""
            
        
            try:
                videoCount =  int(channel["items"][0]["statistics"]["videoCount"]) 
            except Exception as _ex:
                videoCount = 0
        
            try:
                viewCount = int(channel["items"][0]["statistics"]["viewCount"])
            except Exception as _ex:
                viewCount = 0
            
        
            try:
                if channel["items"][0]["statistics"]["hiddenSubscriberCount"] == True:
                    subscriber_count = 0
                subscriber_count = int(channel["items"][0]["statistics"]["subscriberCount"])
            except Exception as _ex:
                subscriber_count = 0
            
            try:
                description = channel["items"][0]["snippet"]["description"] 
            except Exception as _ex:
                description = ""
                
            videos = []
                
            try:
                for video in channel["videos"]:
                    id = ""
                    title = ""
                    like_count = 0
                    view_count = 0
                    comments = 0
                    
                    try:
                        id = video["items"][0]["id"]
                    except Exception as _ex:
                        id = 0
                    
                    try:
                        title = video["items"][0]["snippet"]["title"]
                    except Exception as _ex:
                        title = ""
                        
                    try:
                        like_count = int(video["items"][0]["statistics"]["likeCount"]) 
                    except Exception as _ex:
                        like_count = 0
                        
                    try:
                        view_count = int(video["items"][0]["statistics"]["viewCount"])
                    except Exception as _ex:
                        view_count = 0
                        
                    try:
                        comments = int(video["items"][0]["statistics"]["commentCount"])
                    except Exception as _ex:
                        comments = 0
                    
                    videos.append(Video(id, title, like_count, viewCount, hour, comments) )
                    
            except Exception as _ex:
                videos = None
                
            channels.append(Channel(channel_id, channel_title, viewCount, videoCount, description, subscriber_count, videos))
            
        return channels