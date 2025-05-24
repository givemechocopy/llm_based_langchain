from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os


load_dotenv()

template = "{product}를 홍보하기 위한 종흔 문구를 추천해줘"

# API 키를 환경 변수에서 가져옴
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = PromptTemplate(
    input_variables=["product"],
    template=template,
    openai_api_key=openai_api_key
)

print(prompt.format(product="카메라"))