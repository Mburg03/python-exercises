import streamlit as st
import requests

# nasa api key =  UdYU3EeAim4wp4bwuwd2qvZldZIl2vKu3KZNXQZM
st.title("Nasa Picture of the day!")

url = "https://api.nasa.gov/planetary/apod?api_key=UdYU3EeAim4wp4bwuwd2qvZldZ"\
    "Il2vKu3KZNXQZM"

response = requests.get(url)
content = response.json()

image_url = content["url"]
title = content["title"]
explanation = content["explanation"]
date = content["date"]

image_response = requests.get(image_url)
image_content = image_response.content

with open('./nasa_image.jpg', 'wb') as file:
    file.write(image_content)
    

st.title(title)
st.write(date)
st.image("./nasa_image.jpg")
st.write(explanation)
