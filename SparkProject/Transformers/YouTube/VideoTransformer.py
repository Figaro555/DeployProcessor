from Transformers.AbstractTransformer import AbstractTransformer


class VideoTransformer(AbstractTransformer):
    id = ""
    title = ""

    def transform_to_tuple(self, video):
        try:
            id = video["items"][0]["id"]
        except Exception as _ex:
            id = 0

        try:
            title = video["items"][0]["snippet"]["title"]
        except Exception as _ex:
            title = ""

        return id.replace("'", "''"), title.replace("'", "''")
