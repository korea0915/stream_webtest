import streamlit as st
import numpy as np

st.title("조 추첨 페이지")
st.header("여러분의 참여를 환영합니다.")

colums = st.colums(4)
for c in colums:
    st.text_input("조 추첨 대상")