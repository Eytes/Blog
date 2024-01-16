import requests
import streamlit as st

from config import topic_prefix
from schemas.topics import TopicCreate


@st.cache_data(ttl=60)
def get_all_topic_names() -> list[str]:
    topics_raw = requests.get(topic_prefix + "/")
    return [topic.get("name") for topic in topics_raw.json()]


def create_topic(new_topic: TopicCreate):
    response = requests.post(
        topic_prefix + "/",
        json=new_topic.model_dump(),
    )
    match response.status_code:
        case 201:
            return "Success"
        case _:
            return response.json().get("detail")
