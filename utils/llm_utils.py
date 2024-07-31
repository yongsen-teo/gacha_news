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

