import streamlit as st

from schemas.posts import Post
from urls.posts import get_author_by_post_id


def show_posts_in_expander_with_tab(post: Post):
    expander = st.expander(post.title, expanded=True)
    author_tab, content_tab, comments_tab = expander.tabs(
        [
            "Author",
            "Content",
            "Comments",
        ]
    )

    with author_tab:
        author = get_author_by_post_id(post.id)
        st.text(author.name + "\n" + author.email)

    with content_tab:
        st.write(post.content)

    with comments_tab:
        pass
