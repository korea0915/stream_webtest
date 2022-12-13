import streamlit as st 
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

titanic = sns.load_dataset("titanic")

st.write(titanic)
st.write(titanic.info())