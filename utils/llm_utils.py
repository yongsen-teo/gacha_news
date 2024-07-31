import os

import anthropic
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

env = load_dotenv()

openai_api_key = st.secrets["OPENAI_API_KEY"]
openai_org_id = st.secrets["OPENAI_ORG_ID"]
anthropic_api_key = st.secrets["ANTHROPIC_API_KEY"]
youtube_api_key = st.secrets["YOUTUBE_API_KEY"]

def choose_openai():
    client = OpenAI(
        api_key=openai_api_key,
        organization=openai_org_id,
    )
    return client

def choose_anthropic():
    client = anthropic.Anthropic(api_key=anthropic_api_key)
    return client

def arrange_user_prompt(video_info, transcript):
    """
    Arrange the video info into a prompt for LLM.
    Args:
        video_info (dict): Dictionary containing video information
        game_info (str): Additional information to be added to the prompt
        video_transcript (str): Transcript of the video
    Return:
        str : User Prompt for LLM
    """
    video_title = video_info.get("title", "")
    main_question = f"<video_title>{video_title}</video_title>\n"
    transcript = f"<video_transcript>{transcript}</video_transcript>"

    input_prompt = main_question + transcript
    return input_prompt
