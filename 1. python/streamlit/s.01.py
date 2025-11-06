# pip install stramlit - 터미널 실행   #""cd streamlit"-> streamlit run 파일명"

import streamlit as st
st.title('타이틀')
st.write('첫번째 앱')
st.header("헤더")
st.subheader("서브헤더")
st.button('버튼')
st.checkbox('체크박스')
st.radio('레디오박스', ('a', 'b', 'c'))
st.selectbox('셀렉트박스',('일번', '이번'))
st.slider('슬라이더', 0,100 ,50) # 최대 최소

name = st.text_input('이름을 입력하세요')
st.write(f'안녕하세요 {name}님!')


#streamlit>streamlit run s.01.py ㅝㅗ