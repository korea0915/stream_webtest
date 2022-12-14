import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

## 함수관련
def draw_plot(df, location = '지역선택', size = '크기선택'):
    if (location == '지역선택') & (size == '크기선택'):
        st.image("./opendata/img/sample.jpg")
    elif location == '지역선택':
        # 크기 선택, 구별 확인
        data = df[['자치구 명',f'{size} 거래건수', f'{size} 거래금액']]
        # 거래 건수
        fig1 = px.bar(data, x='자치구 명', y=f'{size} 거래건수')
        fig1.update_traces(marker={"color": "magenta",
                                    "opacity": 0.5})
        # 거래 금액
        fig2 = px.bar(data, x='자치구 명', y=f'{size} 거래금액')
        st.plotly_chart(fig1, theme='streamlit')
        st.plotly_chart(fig2, theme='streamlit')
        # fig1 = px.bar(data, x='자치구 명', y='소형 거래건수')
        # fig2 = px.bar(data, x='자치구 명', y='소형 거래금액')
        # st.plotly_chart(fig1)
        # # st.plotly_chart(fig2)
    elif size == '크기선택':
        # 구 선택, 크기별 확인
        data = pd.DataFrame(df.set_index('자치구 명').T.iloc[1:6,:][location])
        data = data.reset_index().rename(columns = {'index':'크기'})
        # 거래 건수
        fig1 = px.bar(data, x=location, y='크기')
        fig1.update_traces(marker={"color": "magenta",
                                  "opacity": 0.5})
        # 거래 금액
        fig2 = px.bar(data, x=location, y='크기')
        st.plotly_chart(fig1, theme='streamlit')
        st.plotly_chart(fig2, theme='streamlit')
    else:
        # 지역, 크기 둘 다 선택
        data = df[['자치구 명',f'{size} 거래건수', f'{size} 거래금액']]
        data_loc = data[data['자치구 명'] == location]
        # 거래 건수
        fig1 = px.bar(data_loc, x='자치구 명', y=f'{size} 거래건수')
        fig1.update_traces(marker={"color": "magenta",
                                   "opacity": 0.5})
        # 거래 금액
        fig2 = px.bar(data_loc, x='자치구 명', y=f'{size} 거래금액')
        st.plotly_chart(fig1, theme='streamlit')
        st.plotly_chart(fig2, theme='streamlit')

def max_min(location, size):                                  #결론 부분의 들어갈 데이터 가공 후 출력
    data = df.drop(columns= "거래년도")
    data = data.set_index(keys="자치구 명")
    if (location == "지역선택") & (size != "크기선택"):
        maxv = data[f"{size} 거래금액"].max()         #최고 매매가
        maxi = data[f"{size} 거래금액"].idxmax()      #최고 매매가 지역
        minv = data[f"{size} 거래금액"].min()         #최소 매매가
        mini = data[f"{size} 거래금액"].idxmin()      #최소 매매가 지역
        maxc = data[f"{size} 거래건수"].idxmax()      #거래가 가장 많이 된 곳
        minc = data[f"{size} 거래건수"].idxmin()      #거래가 가장 적게 된 곳
        st.write(f"""
                    ### {year} 서울 아파트 매매 거래현황
                    - 제일 인기 있는 지역 :  {maxc}
                    - 제일 인기 없는 지역 :  {minc}

                    - 최고 매매가 : {maxi}지역의 {maxv}원
                    - 최소 매매가 : {mini}지역의 {minv}원     
                """)

    elif (location != "지역선택") & (size == "크기선택"):
        maxv = data.loc[f"{location}", "소형 거래금액":].max()  #최고 매매가
        maxc = data.loc[f"{location}", :"대형 거래건수"].idxmax()  #인기 있는 사이즈
        minv = data.loc[f"{location}", "소형 거래금액":].min()  #최소 매매가
        minc = data.loc[f"{location}", :"대형 거래건수"].idxmin()  #인기 없는 사이즈
        st.write(f"""
                    ### {year}년 {location}지역의 아파트 매매 현황
                    - {location}지역의 최고 매매가 : {maxv}원
                    - {location}지역의 최저 매매가 : {minv}원
                    - {location}지역의 가장 인기있는 사이즈 : {maxc[:4]}
                    - {location}지역의 가장 인기없는 사이즈 : {minc[:4]}
                """)
    else:
        st.write("보여드릴게 없습니다.")




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
            '지역선택', '강동구', '송파구', '강남구', '서초구', '관악구', '동작구', '영등포구', '금천구', '구로구',
            '강서구', '양천구', '마포구', '서대문구', '은평구', '노원구', '도봉구', '강북구', '성북구',
            '중랑구', '동대문구', '광진구', '성동구', '용산구', '중구', '종로구'
        )
    )
size = st.sidebar.selectbox(                     #사이드바 선택박스 크기 선택
    "크기 선택",
        (
            '크기선택', '소형', '중소형', '중형', '중대형', '대형'
        )
    )



#데이터 불러오기, 가공

df = pd.read_csv(f'./opendata/data/df_{year}.csv') #선택한 년도 데이터 불러오기





# 탭에서 데이터 그리기

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])          #탭1으로 그래프로 볼지, 탭2로 데이터 프레임으로 볼지 선택
with tab1:                                             #탭 1 헤더
    if (location == '지역선택') & (size == '크기선택'):
        tab1.subheader(f"{year}년도  그래프: 지역과 크기를 선택해 주세요.")
    elif (location != '지역선택') & (size == '크기선택'):
       tab1.subheader(f"{year}년도 {location}별 매매현황 그래프")
    elif (location == '지역선택') & (size != '크기선택'):
        tab1.subheader(f"{year}년도 {size}별 매매현황 그래프")
    else:
        tab1.subheader(f"{year}년도 {location}지역 ,{size}별 매매현황 그래프")                
    draw_plot(df, location, size)                                #탭 1 그래프 출력

                               #탭 2 헤더
tab2.subheader(f"{year}년도 그래프")                     
tab2.write(df)                                        #탭 2 데이터 출력



with st.expander("결론"):                                #결론 출력(최곳값, 최솟값 등등)
    max_min(location, size)            
