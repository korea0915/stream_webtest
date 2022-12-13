import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
AI26year = [2018,2019,2020]
# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "원하시는 년도를 선택해 주세요",
        (AI26year[0], AI26year[1], AI26year[2])
    )


add_selectbox = st.sidebar.selectbox(
    "지역 선택",
    ("서울", "인천", "등등")
)


tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)

tab1.subheader("A tab with a chart")
tab1.line_chart(data)

tab2.subheader("A tab with the data")
tab2.write(data)

with st.expander("결론"):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg")