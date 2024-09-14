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
        text-align: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="big-font">WELCOME!</p>', unsafe_allow_html=True)

if st.button("Start"):
    st.write("Redirecting...")
    # Replace 'location.py' with a valid URL or endpoint that you want to navigate to.
    st.markdown('<meta http-equiv="refresh" content="0; url=https://www.google.com/maps/dir/11.0256315,77.00412039999999/10.6873489,77.0939825/@11.0256315,77.00412039999999,12z/data=!4m2!4m1!3e9?entry=ttu&g_ep=EgoyMDI0MDkxMS4wIKXMDSoASAFQAw%3D%3D&waypoints=11.0241817,77.0051343|11.0129398,76.9861492|11.0044381,76.9930368|10.9972005,76.9957349|10.997194,76.9958525|10.9647118,76.9876043|10.9498072,77.0000328|10.9241232,76.98286089999999|10.917951,76.9860578|10.8342314,77.0171112|10.746312,77.020006|10.7448453,77.0197603|10.7445227,77.0201866|10.7416404,77.0580423|10.7406532,77.059314|10.7406533,77.05940319999999|10.7399939,77.0603423|10.7303415,77.0688081|10.7257708,77.06795269999999|10.7071304,77.0713308|10.7022968,77.0707381|10.7000676,77.0703809|10.7001793,77.06986189999999|10.6985697,77.06896669999999|10.6918329,77.0682104|10.6916451,77.06859|10.6897099,77.08369069999999|10.6878073,77.0947443">', unsafe_allow_html=True)
