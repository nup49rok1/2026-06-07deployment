from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPEN_API_KEY") 

with st.sidebar:
    # openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")

# 대화 내용을 저장할 messages 변수를 초기화
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# 대화 내용을 아이콘 + 텍스트 형식으로 출력 
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 사용자 입력을 처리
if prompt := st.chat_input():
    # if not openai_api_key:
    #    st.info("Please add your OpenAI API key to continue.")
    #    st.stop()

    client = OpenAI(api_key=api_key)
    # client = OpenAI()

    # 대화 내용에 사용자 입력(질의)을 추가하고, 화면에 출력
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # LLM 질의
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=st.session_state.messages
    )

    # LLM 응답을 대화 내용에 추가하고, 화면에 출력
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
