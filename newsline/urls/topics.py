import requests
import streamlit as st

from config import topic_prefix


@st.cache_data(ttl=60)
def get_all_topics():
    topics_raw = requests.get(topic_prefix + "/")
    return [topic.get("name") for topic in topics_raw.json()]
