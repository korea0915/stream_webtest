import streamlit as st
import numpy as np

st.title("조 추첨 페이지")
st.header("여러분의 참여를 환영합니다.")
colums = st.columns(4)

for idx,col in enumerate(colums):
    for idx2 in range(4):
        col.text_input
        (
            f"조 추첨 대상 {idx+1 +idx2*4}", 
            key=f"{idx+1+idx2*4}"
        )