import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Nguyen Pham Phuong Anh")
    content = ("I am a student at the University Applied Science Fulda.\n"
               "I am studying Wirtschaftsinformatik in the 4th Semester. I am interested in Programming and Data Science Fields.\n"
               "I am looking for a student job or internship in the field of Data Science or Software Development.\n "
               "I am open to new opportunities and challenges. I am a fast learner and I am willing to learn new things.\n"
               "I am a team player and I am able to work independently. Please contact me if you have any opportunities for me. Thank you!\n"
               "Right now i am not having a picture of myself. Feel free to look at my cutest cat")
    st.info(content)

st.write("Below you can find some of the apps I have build in Python. Feel free to contact me")

col3, empty_column, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({'url'})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({'url'})")

