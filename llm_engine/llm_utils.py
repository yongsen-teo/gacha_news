import os

import anthropic
from dotenv import load_dotenv
from openai import OpenAI

env = load_dotenv()

def choose_openai():
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"), organization=os.getenv("OPENAI_ORG_ID")
    )
    return client

def choose_anthropic():
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
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
