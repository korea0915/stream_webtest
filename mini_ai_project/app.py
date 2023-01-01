import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]
def chat_api(yinput):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt="You: What have you been up to?\nFriend: Watching old movies.\nYou: Did you watch anything interesting?\nFriend:",
    temperature=0.5,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    stop=["You:"]
  )
  message = response.choices[0].text
  return message
    
yinput = st.text_input("You: ", "hello, how are you?", key="input")

st.write(chat_api(yinput))