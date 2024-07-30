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
