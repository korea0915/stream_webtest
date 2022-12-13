# https://docs.streamlit.io/library/get-started/main-concepts
# https://docs.streamlit.io/library/cheatsheet
# streamlit 라이브러리 호출
import streamlit as st # st라는 이름으로 사용
import numpy as np

# st.write() 마크다운
st.title("조추첨 페이지")
st.header("여러분의 참여를 환영합니다!")

# 추첨 대상인 13명의 이름을 넣을 수 있는 text_input
# 4 x 4 (row, col)
# 열을 배치하는 메소드
# x = st.columns(n) : n만큼의 컬럼 리스트를 생성


tabs = st.tabs(['참가자'])
columns = tabs[0].columns(4) # 화면을 열로 나누어서 배치
# 가로 4개의 열 -> columns = [col1, col2, col3, col4]
# col1, col2, col3, col4
# enumerate : index, value 묶음
for idx, col in enumerate(columns): # 열의 위치
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