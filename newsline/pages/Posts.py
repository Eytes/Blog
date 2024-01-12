import streamlit as st

from schemas.posts import Post
from urls.posts import get_posts_by_topic_name, get_author_by_post_id
from urls.topics import get_all_topics


def show_posts_in_expander_with_tab(post: Post):
    expander = st.expander(post.title, expanded=True)
    author_tab, content_tab = expander.tabs(["Author", "Content"])

    with author_tab:
        author = get_author_by_post_id(post.id)
        st.text(author.name + "\n" + author.email)

    with content_tab:
        st.write(post.content)


st.title("Posts")

selected_topic = st.selectbox(
    "Choose a topic to view posts on",
    get_all_topics(),
)

for post in get_posts_by_topic_name(selected_topic):
    show_posts_in_expander_with_tab(post)
