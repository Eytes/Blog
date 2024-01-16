from uuid import UUID

import requests
import streamlit as st

from config import topic_prefix
from schemas.topics import TopicCreate, Topic


@st.cache_data(ttl=60)
def get_topics() -> list[Topic]:
    """Получить все тематики"""
    topics_raw = requests.get(topic_prefix + "/")
    return list(map(lambda topic: Topic(**topic), topics_raw.json()))


def get_topics_name() -> list[str]:
    """Получить все названия тематик"""
    topics = get_topics()
    return [topic.name for topic in topics]


def create_topic(new_topic: TopicCreate):
    """Создание тематики"""
    response = requests.post(
        topic_prefix + "/",
        json=new_topic.model_dump(),
    )
    match response.status_code:
        case 201:
            return "Success"
        case _:
            return response.json().get("detail")


@st.cache_data(ttl=3600)
def get_topic_id_by_name(topic_name: str) -> UUID:
    pass
