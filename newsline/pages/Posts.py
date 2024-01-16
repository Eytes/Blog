import streamlit as st

from forms.posts.create import PostCreateForm
from urls.posts import get_posts_by_topic_name
from urls.topics import get_topics_name
from views.posts import show_posts_in_expander_with_tab

st.title("Posts")

posts_tab, create_tab = st.tabs(["Posts", "Create"])

with posts_tab:
    selected_topic = st.selectbox(
        "Choose a topic to view posts on",
        get_topics_name(),
    )

    for post in get_posts_by_topic_name(selected_topic):
        show_posts_in_expander_with_tab(post)

with create_tab:
    PostCreateForm()
