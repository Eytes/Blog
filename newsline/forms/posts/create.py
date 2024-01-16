import streamlit as st
from pydantic import ValidationError

from schemas.posts import PostCreate
from urls.posts import create_post
from urls.topics import (
    get_topics_name,
    get_topic_id_by_name,
)


class PostCreateForm:
    def __init__(self):
        self.__form = st.form("create")
        with self.__form:
            st.title("Create new post")

            if "author_id" not in st.session_state:
                st.session_state.author_id = ""
            if "title" not in st.session_state:
                st.session_state.title = ""
            if "content" not in st.session_state:
                st.session_state.content = ""
            if "topic_id" not in st.session_state:
                st.session_state.topic_id = ""

            st.text_input("Title", key="title")
            st.text_area("Content", key="content")
            st.selectbox("Choose a topic", get_topics_name(), key="topic_name")
            # TODO: сделать авторизацию и потом вытаскивать из данных сессии данные об авторе
            st.text_input("Author ID", key="author_id")

            st.form_submit_button(
                "create",
                on_click=self._write_factory,
            )

    def _write_factory(self):
        title = st.session_state.title
        content = st.session_state.content
        author_id = st.session_state.author_id
        topic_name = st.session_state.topic_name
        if title and content and author_id and topic_name:
            try:
                new_post = PostCreate(
                    author_id=author_id,
                    title=title,
                    content=content,
                    topic_id=get_topic_id_by_name(topic_name),
                )
                return self._correct_topic_write(new_post)
            except ValidationError:
                return self._incorrect_topic_write()
        return self._empty_topic_left_write()

    def _correct_topic_write(self, new_post):
        create_result = create_post(new_post)
        self.__form.write(create_result)

    def _incorrect_topic_write(self):
        self.__form.error("Incorrect data")

    def _empty_topic_left_write(self):
        self.__form.error("There are empty fields left")
