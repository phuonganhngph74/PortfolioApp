import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Nguyen Pham Phuong Anh")
    content = ("I am a student at the University Applied Science Fulda.I am studying Wirtschaftsinformatik in the 4th Semester. I am interested in Programming and Data Science Fields."
               "I am looking for a student job or internship in the field of Data Science or Software Development. I am open to new opportunities and challenges. I am a fast learner and I am willing to learn new things. I am a team player and I am able to work independently. Please contact me if you have any opportunities for me. Thank you!"
               "Right now i am not having a picture of myself. Feel free to look at my cutest cat")
    st.info(content)
