from uuid import UUID

import requests
import streamlit as st

from config import post_prefix
from schemas.authors import Author
from schemas.posts import (
    Post,
    PostCreate,
)


@st.cache_data(ttl=60)
def get_posts_by_topic_name(topic_name: str) -> list[Post | None]:
    if topic_name:
        posts_raw = requests.get(post_prefix + "/topic/" + topic_name)
        return list(map(lambda post_dict: Post(**post_dict), posts_raw.json()))
    return []


@st.cache_data
def get_author_by_post_id(post_id: UUID) -> Author:
    author_raw = requests.get(post_prefix + f"/{str(post_id)}" + "/author")
    return Author(**author_raw.json())


def create_post(new_post: PostCreate) -> str | None:
    if not isinstance(new_post, PostCreate):
        raise ValueError

    new_post = new_post.model_dump()
    new_post["author_id"] = str(new_post["author_id"])
    new_post["topic_id"] = str(new_post["topic_id"])

    response = requests.post(
        post_prefix,
        json=new_post,
    )
    match response.status_code:
        case 201:
            return "Success"
        case _:
            return response.json().get("detail")
