import streamlit as st
import base64
from backend import ShortestPath  
import googlemaps

# API Key
#api_key = ''
gmaps = googlemaps.Client(key=api_key)

def get_base64_image(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_path = 'static/bg.jpg'
base64_image = get_base64_image(img_path)

if 'start_clicked' not in st.session_state:
    st.session_state.start_clicked = False

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

if st.session_state.start_clicked:
    st.markdown('<h1 style="text-align:center;color:white;">Location Input</h1>', unsafe_allow_html=True)

    start_location = st.text_input("Enter Starting Location:", "", key="start_location", placeholder="Starting Location")
    destination_location = st.text_input("Enter Destination Location:", "", key="destination_location", placeholder="Destination Location")

    def get_coordinates(location):
        geocode_result = gmaps.geocode(location)
        if geocode_result:
            location_info = geocode_result[0]['geometry']['location']
            return (location_info['lat'], location_info['lng'])
        else:
            st.write(f"Could not geocode location: {location}")
            return None

    if st.button("Submit"):
        if start_location and destination_location:
            start_coords = get_coordinates(start_location)
            destination_coords = get_coordinates(destination_location)

            if start_coords and destination_coords:
                path_finder = ShortestPath(api_key, start_coords, destination_coords)
                map_url = path_finder.get_directions_and_find_shortest_path()
                
                if map_url:
                    st.markdown(f'<meta http-equiv="refresh" content="0; url={map_url}" />', unsafe_allow_html=True)
                else:
                    st.write("No path found.")
            else:
                st.write("Please ensure both locations are valid.")
        else:
            st.write("Please enter both start and destination locations.")
else:
    st.markdown('<p class="big-font">NAV TRACE!</p>', unsafe_allow_html=True)
    st.markdown('<p class="quote">FIND YOUR SHORTEST PATH</p>', unsafe_allow_html=True)

    if st.button("Start"):
        st.session_state.start_clicked = True
        st.rerun()
