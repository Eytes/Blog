import streamlit as st
from pydantic import ValidationError

from schemas.authors import AuthorCreate
from urls.authors import create_author


class AuthorRegistrationForm:
    def __init__(self):
        self.__form = st.form("registration")
        with self.__form:
            st.title("Registration new author")

            if "nickname" not in st.session_state:
                st.session_state.nickname = ""
            if "email" not in st.session_state:
                st.session_state.email = ""

            st.text_input("Nickname", key="nickname")
            st.text_input("Email", key="email")

            st.form_submit_button(
                "registration",
                on_click=self._write_factory,
            )

    def _write_factory(self):
        nickname = st.session_state.nickname
        email = st.session_state.email
        if nickname and email:
            try:
                new_author = AuthorCreate(
                    name=nickname,
                    email=email,
                )
                return self._correct_author_write(new_author)
            except ValidationError:
                return self._incorrect_author_write()
        return self._empty_field_left_write()

    def _correct_author_write(self, new_author):
        create_result = create_author(new_author)
        self.__form.write(create_result)

    def _incorrect_author_write(self):
        self.__form.error("Incorrect data")

    def _empty_field_left_write(self):
        self.__form.error("There are empty fields left")
