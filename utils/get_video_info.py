import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

# YouTube API setup
api_key = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

def get_channel_id(channel_name):
    request = youtube.search().list(
        q=channel_name,
        type='channel',
        part='id',
        maxResults=1
    )
    response = request.execute()
    return response['items'][0]['id']['channelId']


def get_latest_videos(channel_id, days=7):
    """
    Get the latest videos from a YouTube channel.
    Day-range is currently set to 7 days as default. 
    Input:
        channel_id: str
        days: int
    Output:
        list of dictionaries containing video date, title, and video id
    """
    videos = []
    page_token = None

    SINGAPORE = ZoneInfo("Asia/Singapore")
    end_date = datetime.now(SINGAPORE)
    start_date = end_date - timedelta(days=days)

    start_date_utc = start_date.astimezone(ZoneInfo("UTC"))
    end_date_utc = end_date.astimezone(ZoneInfo("UTC"))

    while True:
        request = youtube.search().list(
            channelId=channel_id,
            type='video',
            order='date',
            part='id,snippet',
            maxResults=50,
            pageToken=page_token,
            publishedAfter=start_date_utc.isoformat(),
            publishedBefore=end_date_utc.isoformat()
        )
        response = request.execute()

        for item in response['items']:
            video_datetime = datetime.fromisoformat(item['snippet']['publishedAt'].replace('Z', '+00:00'))
            video_datetime_sg = video_datetime.astimezone(SINGAPORE)
            video_date = video_datetime_sg.date()

            if not any(v['date'] == video_date for v in videos):
                videos.append({
                    'date': video_date,
                    'title': item['snippet']['title'],
                    'video_id': item['id']['videoId']
                })

        page_token = response.get('nextPageToken')

        if not page_token:
            break

    return sorted(videos, key=lambda x: x['date'], reverse=True)

# Example usage
channel_id = get_channel_id("sweetily")
latest_videos = get_latest_videos(channel_id)

for video in latest_videos:
    print(f"Date: {video['date']}, Title: {video['title']}, URL: https://www.youtube.com/watch?v={video['video_id']}")
