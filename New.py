import streamlit as st

from PIL import Image

with st.form(key="my_form"):
    username = st.text_input("Username")
    password = st.text_input("Password")
    st.form_submit_button("Login")

img = Image.open("new1.png")
new_image = img.resize((400, 400))
st.sidebar.image(new_image)

x = st.number_input("input first number", step= 1)
y = st.number_input("input second number",step = 1)

col1 , col2, col3 = st.columns(3)
with col1:
    if st.button("Add"):
        st.write(x+y)
with col2:      
    if st.button("Subtract"):
        st.write(x-y)
        
with col3:      
    if st.button("Multiplication"):
        st.write(x*y)        
        
        
        
        
        