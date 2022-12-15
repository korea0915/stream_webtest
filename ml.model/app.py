import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/bigdata-young/ai_26th/main/data/insurance.csv')
st.write(df)

import joblib
import os
model_path = f"{os.path.dirname(os.path.abspath(__file__))}/first_model.pkl"
model = joblib.load(model_path)
st.write("## 선형 회귀 모델")
st.write(pd.Series(model.coef_, index=["age", "bmi", "children", "smoker", "sex_male", "region_northwest", "region_northeast", "region_southwest"]))

st.number_input(
    label="나이",
    step=1,
    value=30,
    key='age'
)

st.radio(
    label = "성별",
    option = ["남성", "여성"],
    index = 0,
    key = "sex"
)

st.number_input(
    label="BMI",
    stop=0.1,
    value = 25.0,
    key="bmi"
)

st.number_input(
    label="자녀 수",
    step=1,
    value=1,
    key='children'
)

