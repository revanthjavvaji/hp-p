import streamlit as st
import os
from streamlit_lottie import st_lottie
import json 
from PIL import Image
import time

st.balloons()
time.sleep(1)
st.balloons()
time.sleep(1)
st.balloons()
time.sleep(1)
st.snow()
time.sleep(1.3)
st.snow()
time.sleep(1.3)
st.snow()
time.sleep(1.3)
st.snow()
time.sleep(1)
st.snow()

file_path = __file__
dir_name = os.path.dirname(file_path)
lottie_url= os.path.join(dir_name, "happy_bday.json")

image_path = os.path.join(dir_name, "p_collage.jpg")
image = Image.open(image_path)

lottie_url_1 = os.path.join(dir_name, "bday_anim.json")
with open(lottie_url, "r") as f:
        lottie_json = json.load(f)

if lottie_json is not None:
        st_lottie(lottie_json)
else:
        st.error("Failed to load animation")


with open(lottie_url_1, "r") as f:
    lottie_json = json.load(f)

if lottie_json is not None:
    container = st.container()
    with container:
        st_lottie(lottie_json)
        st.image(image, use_column_width=True)
else:
    st.error("Failed to load animation")
    
st.markdown(
        """
        <style>
@font-face {
  font-family: 'Tangerine';
  font-style: normal;
  font-weight: 400;
  src: url(https://fonts.gstatic.com/s/tangerine/v12/IurY6Y5j_oScZZow4VOxCZZM.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}

    html, body, [class*="css"]  {
    font-family: 'Tangerine';
    font-size: 48px;
    }
    </style>

    """,
        unsafe_allow_html=True,
    )

"# Hello"

"""This font will look different, based on your choice of radio button"""

#st.text('Happy Birthday Pujitha!!! 🥳🎂🎊 Wishing you all the best on your special day.\nMay your year ahead be filled with love, joy, and prosperity.\nKeep smiling 😊 and spread your positivity to everyone around you🌈.\nCheers 🥂 to a fantastic year ahead!')
