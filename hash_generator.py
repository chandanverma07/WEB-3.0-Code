import streamlit as st
import hashlib

# Function to hash the string
def generate_hash(input_string, hash_type):
    if hash_type == 'MD5':
        return hashlib.md5(input_string.encode()).hexdigest()
    elif hash_type == 'SHA1':
        return hashlib.sha1(input_string.encode()).hexdigest()
    elif hash_type == 'SHA256':
        return hashlib.sha256(input_string.encode()).hexdigest()
    # Add more hash types as needed

# Streamlit application starts here
st.title('Hash Generator')

# User input for the string to be hashed
user_input = st.text_input("Enter a string to hash", "")

# Select the type of hash
hash_type = st.selectbox("Choose the hash type", ['MD5', 'SHA1', 'SHA256'])

# Button to generate hash
if st.button('Generate Hash'):
    hash_result = generate_hash(user_input, hash_type)
    st.write(f"The {hash_type} hash of '{user_input}' is:", hash_result)
