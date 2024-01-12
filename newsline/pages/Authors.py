import streamlit as st

from forms.authors.registration import AuthorRegistrationForm

st.title("Authors")

authors_tab, registration_tab = st.tabs(["Authors", "Registration"])

with authors_tab:
    # TODO: сделать вывод авторов
    st.text("Title")

with registration_tab:
    AuthorRegistrationForm()
