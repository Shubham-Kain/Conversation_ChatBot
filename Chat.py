from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="google/gemini-2.5-flash",  # Free model
    temperature=1.0,
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key="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",
    max_completion_tokens=500
)
# st.header("Blue[Chatbot] Interface",divider="rainbow",style="font-size: 35px; font-weight: bold;position:Fixed;top: 0; left: 0; width: 100%; text-align: center;")

st.set_page_config(page_title="Chatbot Interface", page_icon=":robot_face:", )

st.markdown("""
    <h1 style="font-size: 70px; font-weight: bold; top: 0; left: 0; width: 100%; text-align: center;overflow: hidden;z-index: 1000;">
        <span style="color: #FF4B4B;"> Chatbot </span> <span style="color: #5421fe;"> Interface </span>
    </h1>
""", unsafe_allow_html=True)

Chat_history = [
 SystemMessage(content="You are a helpful assistant.Understand the question give the output of user's want to need and no extra information is add. Please answer the user's questions to the best of your ability.")
]

if "messages" not in st.session_state:
 st.session_state.messages = Chat_history

for message in st.session_state.messages:
 if isinstance(message, HumanMessage):
  st.chat_message("human").write(message.content)
 elif isinstance(message, AIMessage):
  st.chat_message("ai").write(message.content)

if user_input := st.chat_input("You: "):
 st.session_state.messages.append(HumanMessage(content=user_input))
 st.chat_message("human").write(user_input)
 response = model.invoke(st.session_state.messages)
 st.session_state.messages.append(AIMessage(content=response.content))
 st.chat_message("ai").write(response.content)