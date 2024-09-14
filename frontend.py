# import streamlit as st
# import base64
# # import backend

# # API_KEY = 'AIzaSyAyHmK4lf7nriSYK_WzZvhNb0IJdUcohwg'

# def get_base64_image(file_path):
#     with open(file_path, "rb") as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# img_path = 'static/bg.jpg'
# base64_image = get_base64_image(img_path)

# # Check if 'start_clicked' is in session state, if not set it to False
# if 'start_clicked' not in st.session_state:
#     st.session_state.start_clicked = False

# st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url("data:image/jpg;base64,{base64_image}");
#         background-size: cover;
#     }}
#     .big-font {{
#         display: flex;
#         justify-content: center;
#         font-size: 85px;
#         color: white;
#     }}
#     .stButton > button {{
#         font-size: 80px;
#         font-weight: bold; /* Make text bold */
#         padding: 20px 100px;
#         background-color: transparent; /* No background */
#         color: white;
#         border: 3px solid white;
#         border-radius: 20px;
#         display: block;
#         margin: 0 auto;
#         cursor: pointer;
#         transition: background 0.3s ease;
#     }}
#     .stButton > button:hover {{
#         background: linear-gradient(90deg, rgba(34,193,195,1) 0%, rgba(45,253,81,1) 100%);
#         color: white;
#     }}
#     .quote {{
#         text-align: center;
#         margin-top: 50px;
#         font-size: 50px;
#         color: yellow !important;
#     }}
#     .custom-input {{
#         font-size: 20px;
#         font-weight: bold;
#         color: white;
#         background-color: transparent;
#         border: 2px solid white; /* White border */
#         border-radius: 5px;
#         padding: 10px;
#         width: 100%;
#         margin-bottom: 20px;
#         transition: all 0.3s ease;
#     }}
#     .custom-input:focus {{
#         color: black;
#         border: 2px solid black;
#         background-color: white;
#     }}
#     .submit-button {{
#         font-size: 30px;
#         padding: 10px 100px;
#         background-color: transparent;
#         color: white;
#         border: 2px solid white; /* White border */
#         border-radius: 5px;
#         cursor: pointer;
#         transition: background 0.3s ease;
#     }}
#     .submit-button:hover {{
#         background: linear-gradient(90deg, rgba(34,193,195,1) 0%, rgba(45,253,81,1) 100%);
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Check if 'start_clicked' is True and show the location.py content
# if st.session_state.start_clicked:
#     st.markdown('<h1 style="text-align:center;color:white;">Location Input</h1>', unsafe_allow_html=True)

#     st.markdown('''
#         <div >
#             <label for="start_location" style="color: white; font-weight: bold; font-size: 20px;">Enter Starting Location:</label>
#             <input type="text" id="start_location" class="custom-input" placeholder="Starting Location">
#         </div>
#         <div style=" margin-top: 20px;">
#             <label for="destination_location" style="color: white; font-weight: bold; font-size: 20px;">Enter Destination Location:</label>
#             <input type="text" id="destination_location" class="custom-input" placeholder="Destination Location">
#         </div>
#         <div style="text-align: center; margin-top: 20px;">
#             <button id="submit_button" class="submit-button">Submit</button>
#         </div>
#     ''', unsafe_allow_html=True)
# else:
#     st.markdown('<p class="big-font">TRACK!</p>', unsafe_allow_html=True)
#     st.markdown('<p class="quote">FIND YOUR SHORTEST PATH</p>', unsafe_allow_html=True)

#     if st.button("Start"):
#         st.session_state.start_clicked = True
#         st.rerun()
import streamlit as st
import base64

# API_KEY = 'AIzaSyAyHmK4lf7nriSYK_WzZvhNb0IJdUcohwg'

def get_base64_image(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_path = 'static/bg.jpg'
base64_image = get_base64_image(img_path)

# Check if 'start_clicked' is in session state, if not set it to False
if 'start_clicked' not in st.session_state:
    st.session_state.start_clicked = False

# CSS styling
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{base64_image}");
        background-size: cover;
    }}
    .big-font {{
        display: flex;
        justify-content: center;
        font-size: 85px;
        color: white;
    }}
    .stButton > button {{
        font-size: 80px;
        font-weight: bold; /* Make text bold */
        padding: 20px 100px;
        background-color: transparent; /* No background */
        color: white;
        border: 3px solid white;
        border-radius: 20px;
        display: block;
        margin: 0 auto;
        cursor: pointer;
        transition: background 0.3s ease;
    }}
    .stButton > button:hover {{
        background: linear-gradient(90deg, rgba(34,193,195,1) 0%, rgba(45,253,81,1) 100%);
        color: white;
    }}
    .quote {{
        text-align: center;
        margin-top: 50px;
        font-size: 50px;
        color: yellow !important;
    }}
    .custom-input {{
        font-size: 20px;
        font-weight: bold;
        color: white;
        background-color: transparent;
        border: 2px solid white; /* White border */
        border-radius: 5px;
        padding: 10px;
        width: 100%;
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }}
    .custom-input:focus {{
        color: black;
        border: 2px solid black;
        background-color: white;
    }}
    .submit-button {{
        font-size: 30px;
        padding: 10px 100px;
        background-color: transparent;
        color: white;
        border: 2px solid white; /* White border */
        border-radius: 5px;
        cursor: pointer;
        transition: background 0.3s ease;
    }}
    .submit-button:hover {{
        background: linear-gradient(90deg, rgba(34,193,195,1) 0%, rgba(45,253,81,1) 100%);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Check if 'start_clicked' is True and show the location input form
if st.session_state.start_clicked:
    st.markdown('<h1 style="text-align:center;color:white;">Location Input</h1>', unsafe_allow_html=True)

    # Streamlit input fields instead of HTML
    start_location = st.text_input("Enter Starting Location:", key="start_loc")
    destination_location = st.text_input("Enter Destination Location:", key="dest_loc")

    if st.button("Submit"):
        if start_location and destination_location:
            st.success(f"Calculating shortest path from {start_location} to {destination_location}...")
            # Call your backend function here (e.g., ShortestPath)
            # path_finder = ShortestPath(API_KEY, start_location, destination_location)
            # path_finder.get_directions_and_find_shortest_path()
        else:
            st.error("Please enter both a starting location and a destination.")
else:
    st.markdown('<p class="big-font">TRACK!</p>', unsafe_allow_html=True)
    st.markdown('<p class="quote">FIND YOUR SHORTEST PATH</p>', unsafe_allow_html=True)

    if st.button("Start"):
        st.session_state.start_clicked = True
        st.rerun()
