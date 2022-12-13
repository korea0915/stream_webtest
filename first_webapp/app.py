##streamlit 라이브러리 불러오기
import streamlit as st

##메인에 글 작성
st.write(
    """
    # stramlit기반의 웹 페이지연습
    ## 마크다운으로 작성
    * 테스트 입니다.
    """
)
st.button('Click me')
##이미지 표시
st.image(
    "https://imagescdn.gettyimagesbank.com/500/201607/a10518606.jpg"
)