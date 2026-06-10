import streamlit as st

st.title("Media - image")

# 서버 이미지
st.image("../data/cat.jpg", caption="This is a cat")

# 웹 이미지
image_url = "https://img.magnific.com/free-photo/adorable-kitty-looking-like-it-want-hunt_23-2149167099.jpg?semt=ais_hybrid&w=740&q=80"
st.image(image_url, caption="웹 이미지")