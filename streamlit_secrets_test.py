import streamlit as st

print("All secrets:", st.secrets["OPENAI"])
print("Keys in secrets:", st.secrets.keys())
