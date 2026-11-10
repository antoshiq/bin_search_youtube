import pandas as pd
from models import MyHashMap, video

df = pd.read_csv('youtube_video.csv')

def build_hash_index(values):
    index = MyHashMap()

    for i in df.itertuples():
        v = video(i.title, f"https://youtube.com/watch?v={i.video_id}", i.channel_name, i.channel_id, i.view_count, i.like_count, i.comment_count)

        index.put(i.video_id, v)

    return index

size = df.shape

unique_field = "video_id"
series = df[unique_field]
keys = series.tolist()

hash_index = build_hash_index(keys)

def get_item_by_id(id):

    return hash_index.get(id)

