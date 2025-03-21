import streamlit as st
from click import prompt

from utils import get_chat_response
from langchain.memory import ConversationBufferMemory

st.title("💬克隆ChatGPT")

with st.sidebar:
    open_api_key = st.text_input("请输入OpenAI API Key",type="password")
    st.markdown("[获取OpenAI API key](https://platform.openai.com/account/api-keys)")
    # st.markdown("[获取OpenAI API key](https://platform.openai.com/account/api-keys)")

# memory = ConversationBufferMemory(return_messages=True)

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role":"ai","content":"你好，我是你的ai助手，有什么可以帮你的吗？"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not open_api_key:
        st.info()
        st.stop()
    st.session_state["messages"].append({"role":"human","content":prompt})
    st.chat_message("human").write(prompt)

    with st.spinner(text="ai正在思考中..."):
        response = get_chat_response(prompt,st.session_state["memory"],open_api_key)

        msg = {"role":"ai","content":response}
        st.session_state["messages"].append(msg)
        st.chat_message("ai").write(response)