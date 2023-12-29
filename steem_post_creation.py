import streamlit as st
from steem import Steem
from steem.commit import Commit

# Function to create a post on Steemit
def create_post(username, posting_key, title, body, tags):
    """ Create a post on Steemit """
    steem = Steem(keys=[posting_key])
    commit = Commit(steem)
    
    try:
        commit.post(title=title, body=body, author=username, tags=tags)
        return True, "Post successfully created on Steemit."
    except Exception as e:
        return False, f"Error: {e}"

# Streamlit UI
st.title("Steemit Post Creator")

# User inputs
username = st.text_input("Steemit Username")
posting_key = st.text_input("Posting Key", type="password")
title = st.text_input("Post Title")
body = st.text_area("Post Body")
tags = st.text_input("Tags (comma-separated)")

# Button to create post
if st.button("Create Post"):
    success, message = create_post(username, posting_key, title, body, tags.split(","))
    if success:
        st.success(message)
    else:
        st.error(message)
