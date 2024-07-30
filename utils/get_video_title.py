import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

# YouTube API setup
api_key = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_title(video_url):
    # Extract video ID from URL
    video_id = None
    if 'youtube.com/watch?v=' in video_url:
        video_id = video_url.split('v=')[1].split('&')[0]
    elif 'youtu.be/' in video_url:
        video_id = video_url.split('/')[-1]

    if not video_id:
        return "Invalid YouTube URL"

    try:
        # Call the videos().list method to retrieve video details
        request = youtube.videos().list(
            part="snippet",
            id=video_id
        )
        response = request.execute()

        # Check if the response contains any items
        if 'items' in response and len(response['items']) > 0:
            # Extract the title from the response
            print(f"RESPONSE: {response}")
            title = response['items'][0]['snippet']['title']
            return title
        else:
            return "Video not found"

    except Exception as e:
        return f"An error occurred: {str(e)}"

print(get_video_title("https://youtu.be/uCzGI6M8te4"))
