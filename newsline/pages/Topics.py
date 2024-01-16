import pandas as pd
import streamlit as st

from forms.topics.create import TopicCreateForm
from urls.topics import get_topics_name

st.title("Topics")

topics_tab, create_tab = st.tabs(["Topics", "Create"])

with topics_tab:
    topic_names = get_topics_name()
    df = pd.DataFrame(
        {
            "name": topic_names,
        }
    )
    st.dataframe(
        df,
        hide_index=True,
        use_container_width=True,
    )

with create_tab:
    TopicCreateForm()
