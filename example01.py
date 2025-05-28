"""
这段代码是一个基于 Streamlit 的聊天机器人应用，
它通过状态管理来保存聊天记录，并且可以显示多条消息而不是覆盖之前的记录。
# pip install langchain langchain-openai langchain-community
详细介绍这段代码的每个部分，包括代码的功能、实现逻辑以及相关的知识点。
streamlit run example01.py
"""
#
# import random
# import streamlit as st
# from dotenv import load_dotenv
# from openai import OpenAI
#
# # 这个没有绘画管理，只能显示一条消息，再输入就会覆盖
# # 从预定义的响应列表中随机选择一个响应。
# def generate_response():
#     resp_list = ['hello','goodbye','赶紧滚犊子']
#     index= random.randrange(len(resp_list))
#     return resp_list[index]
#
# load_dotenv()
# # 初始化 OpenAI 客户端
# client = OpenAI(base_url='https://twapi.openai-hk.com/v1')
#
#
# st.title('# 我的ChatGPT')
#
#
# # 进行绘画状态管理，session_state
# if 'message' not in st.session_state:
#     st.session_state['message'] = [{'role':'ai','content':'你好主人，我是你的AI助手，我叫小美'}]
#
# for message in st.session_state['messages']:
#     role, content = message['role'],message['content']
#     st.chat_message(role).write(content)
#
# # st.chat_message('ai').write('你好，我是你的AI助手，我叫小江')
#
# user_input = st.chat_input()
# if user_input:
#     st.chat_message('human').write(user_input)
#     st.session_state['message'].append({'role':'human','content':user_input})
#     with st.spinner('AI正在思考，请等待....'):
#         if 'history' in st.session_state:
#             user_input = st.session_state['history'] + '\n' + user_input
#         resp_from_ai = generate_response()
#         st.chat_message('ai').write(resp_from_ai)
#         st.session_state['message'].append({'role':'ai','content':resp_from_ai})


# 再次进行改写
import streamlit as st
from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI







def get_ai_response(user_prompt):
    model = ChatOpenAI(
        model='gpt-4o-mini',
        api_key=st.session_state['API_KEY'],
        base_url='https://twapi.openai-hk.com/v1'
    )
    chain = ConversationChain(llm=model, memory=st.session_state['memory'])
    return chain.invoke({'input': user_prompt})['response']


st.title('我的ChatGPT')

with st.sidebar:
    api_key = st.text_input('请输入你的Key：', type='password')
    st.session_state['API_KEY'] = api_key

if 'messages' not in st.session_state:
    st.session_state['messages'] = [{'role': 'ai', 'content': '你好主人，我是你的AI助手，我叫小美'}]
    st.session_state['memory'] = ConversationBufferMemory(return_message=True)

for message in st.session_state['messages']:
    role, content = message['role'], message['content']
    st.chat_message(role).write(content)

user_input = st.chat_input()
if user_input:
    if not api_key:
        st.info('请输入自己专属的Key！！！')
        st.stop()
    st.chat_message('human').write(user_input)
    st.session_state['messages'].append({'role': 'human', 'content': user_input})
    with st.spinner('AI正在思考，请等待……'):
        resp_from_ai = get_ai_response(user_input)
        st.session_state['history'] = resp_from_ai
        st.chat_message('ai').write(resp_from_ai)
        st.session_state['messages'].append({'role': 'ai', 'content': resp_from_ai})







# 最开始的
# import random
# import string
#
# import streamlit as st
#
# def generate_word(length):
#     return ''.join(random.choice(string.asscii_lowercase,k=length))
#
#
# def generate_response():
#     words_cnt = random.randrange(1,10)
#     temp = [generate_word(random.randrdange(3,10)) for _ in range(words_cnt)]
#     return ' '.join(temp)
#
# st.title('# 我的ChatGPT')
#
# st.chat_message('ai').write('你好，我是你的AI助手，我叫小江')
#
# user_input = st.chat_input()
# if user_input:
#     st.chat_message('human').write(user_input)
#     st.chat_message('ai').write(generate_response())

