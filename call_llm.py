import os
from langchain_community.chat_models import ChatOpenAI

# API 키를 환경 변수에서 가져옴
openai_api_key = os.getenv("OPENAI_API_KEY")


llm1 = ChatOpenAI(
    temperature=0,      # 모델의 창의성
    model_name='gpt-4',  # 모델명
    openai_api_key=openai_api_key
)

prompt = "진희는 강아지를 키우고 있습니다. 진희가 키우고 있는 동물은?"
print(llm1.predict(prompt))