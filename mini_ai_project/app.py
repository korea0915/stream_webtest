import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openai
##open chatGPT api
openai.api_key = st.secrets["OPENAI_API_KEY"]
def chat_api(yinput):
  response = openai.Completion.create(
  model="text-curie-001",
  prompt=yinput,
  temperature=0.8,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
  )
  message = response.choices[0].text
  return message
    
yinput = st.text_input("You: ", "hello, how are you?", key="input")

st.write(chat_api(yinput))

###코드 시작
df = pd.read_csv("/mini_ai_project/data/train.csv")
st.wirte(df.head())