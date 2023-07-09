import streamlit as st
import os
from streamlit_lottie import st_lottie
import json 
from PIL import Image

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
    

st.text('Happy Birthday Pujitha!!! 🥳🎂🎊 Wishing you all the best on your special day.\nMay your year ahead be filled with love, joy, and prosperity.\nKeep smiling 😊 and spreading your positivity to everyone around you🌈.\nCheers 🥂 to a fantastic year ahead!')
