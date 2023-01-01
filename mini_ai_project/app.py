import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import openai

# openai.organization = "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"
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = ("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")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Convert this text to a programmatic command:\n\nExample: Ask Constance if we need some bread\nOutput: send-msg `find constance` Do we need some bread?\n\nReach out to the ski store and figure out if I can get my skis fixed before I leave on Thursday",
  temperature=0,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.2,
  presence_penalty=0.0,
  stop=["\n"]
)