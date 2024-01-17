import streamlit as st
from pydantic import ValidationError

from schemas.topics import TopicCreate
from urls.topics import create_topic


class TopicCreateForm:
    def __init__(self):
        self.__form = st.form("create")
        with self.__form:
            st.title("Create new topic")

            if "name" not in st.session_state:
                st.session_state.name = ""

            st.text_input("Topic name", key="name")

            st.form_submit_button(
                "create",
                on_click=self._write_factory,
            )

    def _write_factory(self):
        name = st.session_state.name
        if name:
            try:
                new_topic = TopicCreate(name=name)
                return self._correct_topic_write(new_topic)
            except ValidationError:
                return self._incorrect_topic_write()
        return self._empty_topic_left_write()

    def _correct_topic_write(self, new_topic):
        create_result = create_topic(new_topic)
        self.__form.write(create_result)

    def _incorrect_topic_write(self):
        self.__form.error("Incorrect data")

    def _empty_topic_left_write(self):
        self.__form.error("There are empty fields left")
