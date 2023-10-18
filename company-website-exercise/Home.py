import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.header("The Best Company!")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in velit auctor, aliquet eros eget, sagittis eros. Suspendisse potenti. Nulla facilisi. Quisque id est ut nulla gravida rhoncus. Maecenas blandit dolor nec dolor facilisis, et bibendum purus efficitur. Vivamus nec libero vel sapien convallis malesuada. Sed eu odio ligula. Suspendisse aliquam fringilla dolor, a bibendum urna dignissim id. Nulla facilisi. Sed vehicula, elit eget blandit consequat, dolor urna semper urna, nec eleifend dui lorem in arcu. Vivamus ut nunc ac neque vehicula iaculis. Integer nec tellus eu est vulputate dictum. In hac habitasse platea dictumst. Vivamus egestas euismod mauris ut bibendum. Vivamus euismod nunc nec bibendum. Sed non nisl malesuada, euismod ligula sed, tincidunt lectus.")
st.markdown("<h3>Our Team</h3>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
df = pd.read_csv("./data.csv", sep=',')

with col1:
    for index, row in df[:4].iterrows():
        st.write(f"<h3>{row['first name'].capitalize()} {row['last name'].capitalize()}</h3>", unsafe_allow_html=True)
        st.write(f"{row['role']}")
        st.image("./images/" + row['image'])
        
with col2:
    for index, row in df[4:8].iterrows():
        st.write(f"<h3>{row['first name'].capitalize()} {row['last name'].capitalize()}</h3>", unsafe_allow_html=True)
        st.write(f"{row['role']}")
        st.image("./images/" + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        st.write(f"<h3>{row['first name'].capitalize()} {row['last name'].capitalize()}</h3>", unsafe_allow_html=True)
        st.write(f"{row['role']}")
        st.image("./images/" + row['image'])
    