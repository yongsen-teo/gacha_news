import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

from llm_engine.summarizer import summarizer
from utils.get_video_title import get_video_title


def get_youtube_id(url):
    # Extract video ID from YouTube URL
    if "youtu.be" in url:
        return url.split("/")[-1]
    elif "youtube.com" in url:
        return url.split("v=")[-1].split("&")[0]
    return None

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry['text'] for entry in transcript])
    except Exception as e:
        return f"Error: {str(e)}"

st.title("Gacha News Summarizer")

col1, col2 = st.columns([3, 1])

with col1:
    url = st.text_input("Enter YouTube URL", key="url_input")
with col2:
    button = st.button("Enter")

# Check if the button is clicked or Enter key is pressed
if button or (url and st.session_state.url_input != st.session_state.get('previous_url', '')):

    if url:
        video_id = get_youtube_id(url)
        video_title = get_video_title(url)

        if video_id:
            transcript = get_transcript(video_id)
            summarized_notes = summarizer(video_title=video_title,
                                          video_transcript=transcript)
            st.markdown(summarized_notes)

            # allowing markdown to be shown
            # st.text_area("Bite-size Info", st.markdown(summarized_notes), height=300)

        else:
            st.error("Invalid YouTube URL")
    else:
        st.warning("Please enter a YouTube URL")

    # Store the current URL to check for changes
    st.session_state['previous_url'] = url
