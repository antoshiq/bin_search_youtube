import pandas as pd
from models import video

df = pd.read_csv('youtube_video.csv')

def views_binary_search(views_count):
    """ 

    Бинпоиск по просмотрам. 
    Ищем видео с конкретным количеством просмотров большим чем views_count.
    Возвращаем таблицу с видео, у которых количество просмотров больше чем views_count.
    
    """


    sorted_df = df.sort_values("view_count", ascending=True)

    left, right = 0, len(df) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = sorted_df.iloc[mid]["view_count"]

        if mid_value > views_count:
            result = mid_value
            right = mid - 1
        else:
            left = mid + 1

    return sorted_df[sorted_df["view_count"] >= result]


def likes_binary_search(likes_count):
    """ 

    Бинпоиск по лайкам. 
    Ищем видео с конкретным количеством лайков большим чем like_count.
    Возвращаем таблицу с видео, у которых количество лайков больше чем like_count.
    
    """


    sorted_df = df.sort_values("like_count", ascending=True)

    left, right = 0, len(df) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = sorted_df.iloc[mid]["like_count"]

        if int(mid_value) > int(likes_count):
            result = mid_value
            right = mid - 1
        else:
            left = mid + 1

    return sorted_df[sorted_df["like_count"] >= result]


def comments_binary_search(comment_count):
    """ 

    Бинпоиск по кол-ву комментариев. 
    Ищем видео с конкретным количеством комментариев большим чем comment_count.
    Возвращаем таблицу с видео, у которых количество комментариев больше чем comment_count.
    
    """


    sorted_df = df.sort_values("comment_count", ascending=True)

    left, right = 0, len(df) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = sorted_df.iloc[mid]["comment_count"]

        if int(mid_value) > int(comment_count):
            result = mid_value
            right = mid - 1
        else:
            left = mid + 1

    return sorted_df[sorted_df["comment_count"] >= result]


def engagmement_rate_binary_search(engagement_rate):
    """
    
    Бинпоиск по коэффициенту вовлеченности
    Ищем видео с конкретным коэффициентом вовлеченности большим чем engagement_rate.
    Возвращаем таблицу с видео, у которых коэффициент вовлеченности больше чем engagement_rate.
    
    """

    engagement_rate = float(engagement_rate)
    df["engagement_rate"] = (df["like_count"] + df["comment_count"]) / df["view_count"]

    sorted_df = df.sort_values("engagement_rate", ascending=True)

    left, right = 0, len(df) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = float(sorted_df.iloc[mid]["engagement_rate"])

        if mid_value > engagement_rate:
            result = mid_value
            right = mid - 1
        else:
            left = mid + 1

    return sorted_df[sorted_df["engagement_rate"] >= result]


def pack_result(df, count):

    result = []
    for i in df.head(count).itertuples():
        v = video(i.title, f"https://youtube.com/watch?v={i.video_id}", i.channel_name, i.channel_id, i.view_count, i.like_count, i.comment_count)
        result.append(v)

    return result


def get_packed_views(views, count):

    return pack_result(views_binary_search(views), count)

def get_packed_comms(comms, count):

    return pack_result(comments_binary_search(comms), count)

def get_packed_likes(likes, count):

    return pack_result(likes_binary_search(likes), count)

def get_packed_engage(engage, count):

    return pack_result(engagmement_rate_binary_search(engage), count)

