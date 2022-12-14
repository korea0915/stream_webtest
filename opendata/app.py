import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 선택 옵션 데이터

AI26year = [2018,2019,2020]
AI26location = ['강동구', '송파구', '강남구', '서초구', '관악구', '동작구', '영등포구', '금천구', '구로구',
                '강서구', '양천구', '마포구', '서대문구', '은평구', '노원구', '도봉구', '강북구', '성북구',
                '중랑구', '동대문구', '광진구', '성동구', '용산구', '중구', '종로구']


#사이드바에서 원하는 데이터 옵션 선택하기
with st.sidebar:                    #사이드바 라디오 년도 선택
    year = st.radio(
        "원하시는 년도를 선택해 주세요",
        (AI26year[0], AI26year[1], AI26year[2])
    )

location = st.sidebar.selectbox(             #사이드바 선택박스 지역 선택
        "지역 선택",
        (
            '강동구', '송파구', '강남구', '서초구', '관악구', '동작구', '영등포구', '금천구', '구로구',
            '강서구', '양천구', '마포구', '서대문구', '은평구', '노원구', '도봉구', '강북구', '성북구',
            '중랑구', '동대문구', '광진구', '성동구', '용산구', '중구', '종로구'
        )
    )
size = st.sidebar.selectbox(                     #사이드바 선택박스 크기 선택
    "크기 선택",
        (
            '소형', '중소형', '중형', '중대형', '대형'
        )
    )


#데이터 불러오기, 가공

df = pd.read_csv(f'./opendata/data/df_{year}.csv') #선택한 년도 데이터 불러오기





# 탭에서 데이터 그리기

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])          #탭으로 그래프로 볼지 데이터 프레임으로 볼지 선택
data = np.random.randn(10, 1)                          #데이터 입력
 
tab1.subheader(f"{year}년도 {location}지역 매매 현황 그래프")                    #탭 1 헤더
tab1.line_chart(data)                                   #탭 1 그래프 출력

tab2.subheader(f"{year}년도 {location}지역 매매 현황 데이터")                   #탭 2 헤더
tab2.write(df)                                        #탭 2 데이터 출력

with st.expander("결론"):                                #결론 출력(최곳값, 최솟값 등등)
    st.write(f"""
                최고 매매가: max값
                최소 매매가: min값
        최고 많이 팔린 크기:  max값
        제일 적게 팔린 크기:  min값
    """)
    st.image("./opendata/img/exit.png")
