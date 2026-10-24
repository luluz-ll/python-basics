import streamlit as st
from llm_utils import ask

st.title("中译英翻译助手")

# ① 初始化（只在第一次执行时）
if "result" not in st.session_state:
    st.session_state.result = ""

text = st.text_area("输入要翻译的中文", height=150)

if st.button("翻译"):
    with st.spinner("翻译中，请稍候..."):
        # ② 存进 session_state（不是存普通变量）
        st.session_state.result = ask(
            text,
            "你是专业中译英翻译。只输出译文，不加解释、不加引号、不给多个版本。"
        )

# ③ 只要状态里有结果，就显示
if st.session_state.result:
    st.write(st.session_state.result)