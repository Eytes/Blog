from uuid import UUID

import requests
import streamlit as st

from config import post_prefix
from schemas.authors import Author
from schemas.posts import Post


@st.cache_data(ttl=60)
def get_posts_by_topic_name(topic_name: str) -> list[Post | None]:
    if topic_name:
        posts_raw = requests.get(post_prefix + "/topic/" + topic_name)
        return list(map(lambda post_dict: Post(**post_dict), posts_raw.json()))
    return []


@st.cache_data
def get_author_by_post_id(post_id: UUID):
    author_raw = requests.get(post_prefix + f"/{str(post_id)}" + "/author")
    return Author(**author_raw.json())
