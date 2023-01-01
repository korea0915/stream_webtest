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
  prompt=prompt="Product description: A home milkshake maker\nSeed words: fast, healthy, compact.\nProduct names: HomeShaker, Fit Shaker, QuickShake, Shake Maker\n\nProduct description: A pair of shoes that can fit any foot size.\nSeed words: adaptable, fit, omni-fit."
  temperature=0,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.2,
  presence_penalty=0.0,
  stop=["\n"]
  )
  message = response.choices[0].text
  return message
    
yinput = st.text_input("You: ", "hello, how are you?", key="input")

st.write(chat_api(yinput))