import streamlit as st
import os

from dotenv import load_dotenv

#llm 파일
from llm import get_ai_message




st.set_page_config(
    page_title="소득세 챗봇",
    page_icon = ":guardsman:", #이모지 아이콘
    layout = "wide", #레이아웃 설정
    initial_sidebar_state="expanded" #사이드바 초기 상태
)

st.title("Streamlit 기본 예제")
st.caption("소득세에 관련된 모든 것을 답변해 드립니다.")


load_dotenv()

# pinecone_api_key = os.getenv('PINECONE_API_KEY')
# pc = Pinecone(api_key=pinecone_api_key)


#세션 상태에 대화 이력 없으면 리스트 초기화
if "message_list" not in st.session_state:
    st.session_state.message_list = []
    
    


#print(f"before == {st.session_state.message_list}")

# 지금까지의 대화를 챗창에 다시 출력
for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"])
#message를 가져와서 write 한다 -> 메시지가 쌓인다...

    
    
    
if user_question := st.chat_input(placeholder="소득세에 관련된 궁금한 내용을 말씀해 주세요."):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content" : user_question })
    
    
    with st.spinner("답변을 생성하는 중입니다."):
        ai_response = get_ai_message(user_question)
        with st.chat_message('ai'):
            ai_message = st.write_stream(ai_response) #write 대신 write_stream 사용
        st.session_state.message_list.append({"role": "ai", "content" : ai_message})
    

