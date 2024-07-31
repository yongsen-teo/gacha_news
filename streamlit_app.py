import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

from llm_engine.summarizer import summarizer
from utils.get_video_title import get_video_title

openai_api_key = st.secrets["OPENAI_API_KEY"]
openai_org_id = st.secrets["OPENAI_ORG_ID"]
anthropic_api_key = st.secrets["ANTHROPIC_API_KEY"]
youtube_api_key = st.secrets["YOUTUBE_API_KEY"]

def get_youtube_id(url):
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

video_title = st.text_input("Enter youtube title", key="video_title_input")

# Check if the button is clicked or Enter key is pressed
if button or (url and st.session_state.url_input != st.session_state.get('previous_url', '')):

    if url:
        video_id = get_youtube_id(url)

        # TODO: add the VIDEO TITLE WELL (TEST MORE)
        # if not --> then just use user input 
        # 
        #
        # video_title = get_video_title(url)

        if video_id:
            transcript = get_transcript(video_id)
            summarized_notes = summarizer(video_title=video_title,
                                          video_transcript=transcript)
            st.markdown(summarized_notes)
        else:
            st.error("Invalid YouTube URL")
    else:
        st.warning("Please enter a YouTube URL")

    st.session_state['previous_url'] = url
