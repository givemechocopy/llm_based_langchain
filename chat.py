import streamlit as st
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

# 환경 변수 로드
load_dotenv()

# API 키를 환경 변수에서 가져옴
openai_api_key = os.getenv("OPENAI_API_KEY")

# 페이지 설정
st.set_page_config(page_title="🦜🔗 뭐든지 질문하세요~ ")
st.title('🦜🔗 뭐든지 질문하세요~ ')

def generate_response(input_text):
    # openai_api_key 직접 전달
    llm = ChatOpenAI(
        temperature=0,  # 창의성 0으로 설정
        model_name='gpt-4o',  # 모델명
        openai_api_key=openai_api_key
    )
    st.info(llm.predict(input_text))

with st.form('Question'):
    text = st.text_area('질문 입력:', 'What types of text models does OpenAI provide?') #첫 페이지가 실행될 때 보여줄 질문
    submitted = st.form_submit_button('보내기')
    generate_response(text)
    if submitted:
        generate_response(text)

