import pandas as pd
import streamlit as st

from forms.authors.registration import AuthorRegistrationForm
from urls.authors import get_authors

st.title("Authors")

authors_tab, registration_tab = st.tabs(["Authors", "Registration"])

with authors_tab:
    authors = get_authors()
    df = pd.DataFrame(
        {
            "name": [author.name for author in authors],
            "email": [author.email for author in authors],
        }
    )
    st.dataframe(
        df,
        hide_index=True,
        use_container_width=True,
    )


with registration_tab:
    AuthorRegistrationForm()
