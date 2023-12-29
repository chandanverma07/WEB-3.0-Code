import streamlit as st
from steem import Steem

# Initialize Steem object

#s = Steem(keys=['<private_posting_key>', '<private_active_key>'])
s = Steem(keys=['5JmWx7EX8VWn3kkKpY77weBAiYGsTEcv42rSvAbq8UN63VRDZMq','5HqWijN8ZWdoHvi5CbUiuMgHw8aSXuNsHRhyUwMicas4UhStGAH'])

def fetch_posts(tag, limit=5):
    """ Fetches posts from Steemit with the given tag """
    posts = s.get_discussions_by_created({"tag": tag, "limit": limit})
    return posts

def display_posts(posts):
    """ Display posts in the Streamlit app """
    for post in posts:
        st.subheader(post['title'])
        st.write(f"Author: {post['author']}")
        st.write(post['body'][:200] + "...")
        st.write(f"[Read more](https://steemit.com{post['url']})")
        st.markdown("---")

# Streamlit UI
st.title("Steemit Tag Explorer")

tag = st.sidebar.text_input("Enter a tag to search:", "python")
limit = st.sidebar.slider("Number of posts to fetch:", min_value=1, max_value=10, value=5)

if st.sidebar.button("Fetch Posts"):
    with st.spinner('Fetching posts...'):
        posts = fetch_posts(tag, limit)
        display_posts(posts)
