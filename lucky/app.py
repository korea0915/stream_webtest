import streamlit as st
import numpy as np

st.title("조 추첨 페이지")
st.header("여러분의 참여를 환영합니다.")
colums = st.columns(4)

for idx, col in enumerate(colums): # 열의 위치
    # 이중 for문 (for문 안에 for문)
    # col.text_input(f"조 추첨 대상 {idx+1}", key=idx)
    for idx2 in range(4):
        # key가 겹치면 안 됨
        # col 안에 메소드를 통해서 요소들을 생성해주겠다
        col.text_input(
            f"조 추첨 대상 {idx+1 + idx2 * 4}",
            key=f"n{idx+1 + idx2 * 4}"
        ) # 4번 호출됨
# 13명이 소속될 조 이름을 넣을 위치
st.write(st.session_state)
# <추첨 버튼>
# 13개의 짝을 지어서 표시해줄 그래픽