from langchain_community.chat_models import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv
import os

# 환경 변수 로드
load_dotenv()

# API 키를 환경 변수에서 가져옴
api_key = os.getenv("OPENAI_API_KEY")

# 문서 로드
loader = TextLoader("data/AI.txt")
documents = loader.load()


# 문서 분할 함수
def split_docs(documents, chunk_size=1000, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return docs


# 문서 분할
docs = split_docs(documents)

# 임베딩
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", api_key=api_key)

# 벡터 저장소
db = Chroma.from_documents(docs, embeddings)

# LLM 설정
llm = ChatOpenAI(model_name="gpt-4", api_key=api_key)

# QA 체인 로드
chain = load_qa_chain(llm, chain_type="stuff", verbose=True)

# 질의 및 응답
query = "AI란?"
matching_docs = db.similarity_search(query)
answer = chain.run(input_documents=matching_docs, question=query)

print(answer)
