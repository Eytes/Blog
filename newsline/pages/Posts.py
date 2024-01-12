import streamlit as st

from urls.posts import get_posts_by_topic_name
from urls.topics import get_all_topics
from views.posts import show_posts_in_expander_with_tab

st.title("Posts")

selected_topic = st.selectbox(
    "Choose a topic to view posts on",
    get_all_topics(),
)

for post in get_posts_by_topic_name(selected_topic):
    show_posts_in_expander_with_tab(post)
