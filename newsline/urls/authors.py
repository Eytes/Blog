import requests
import streamlit as st

from config import author_prefix
from schemas.authors import AuthorCreate, Author


def create_author(new_author: AuthorCreate) -> str:
    response = requests.post(
        author_prefix,
        json=new_author.model_dump(),
    )
    match response.status_code:
        case 201:
            return "Success"
        case _:
            return response.json().get("detail")


@st.cache_data(ttl=10)  # Обновление данных в кеше каждые 10 сек
def get_authors() -> list[Author]:
    response = requests.get(author_prefix)
    return list(map(lambda author: Author(**author), response.json()))
