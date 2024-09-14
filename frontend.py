import streamlit as st
import base64

def get_base64_image(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_path = 'static/bg.jpg'
base64_image = get_base64_image(img_path)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{base64_image}");
        background-size: cover;
    }}
    .big-font {{
        margin-left:-380px;
        margin-top:-80px;
        font-size: 100px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="big-font">WELCOME!</p>', unsafe_allow_html=True)

if st.button("Start"):
    st.write("Redirecting...")
    # Replace 'location.py' with a valid URL or endpoint that you want to navigate to.
    st.markdown('<meta http-equiv="refresh" content="0; url=http://your-url-here.com">', unsafe_allow_html=True)
