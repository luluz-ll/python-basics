import os
import streamlit as st
from llm_utils import ask


# ---------- 1. 读文件 + 切块（缓存，只算一次）----------
@st.cache_data
def load_chunks():
    files = os.listdir("notes")
    all_texts = []
    for name in files:
        path = os.path.join("notes", name)
        with open(path, "r", encoding="utf-8") as f:
            all_texts.append(f.read())
    materials = "\n\n".join(all_texts)
    return materials.split("\n\n")


# ---------- 2. 检索 ----------
STOP_WORDS = ["为什么", "什么", "怎么", "如何", "哪些", "是否", "的", "了", "是"]


def clean_question(q):
    for w in STOP_WORDS:
        q = q.replace(w, "")
    return q


def score(chunk, question):
    hit = 0
    for i in range(len(question) - 1):
        if question[i:i + 2] in chunk:
            hit += 1
    return hit


def retrieve(question, chunks, top_k=5):
    q = clean_question(question)
    scored = []
    for i, c in enumerate(chunks):
        scored.append((score(c, q), i, c))
    scored.sort(reverse=True)
    return scored[:top_k]


# ---------- 3. 页面 ----------
chunks = load_chunks()

st.title("我的知识库问答")
st.caption(f"知识库共 {len(chunks)} 个段落，来自 notes/ 文件夹")

question = st.text_input("问点关于你笔记的问题")

if st.button("提问"):
    if not question.strip():
        st.warning("请先输入问题")
    else:
        with st.spinner("检索中，请稍候..."):
            top = retrieve(question, chunks)
            context = "\n\n".join([c for s, i, c in top if s > 0])

            prompt = f"""请根据下面的资料回答问题。
如果资料里没有答案，就回答"资料中没有相关内容"。

资料：
{context}

问题：{question}"""

            answer = ask(
                prompt,
                "你是一个基于资料回答问题的助手。只根据资料回答，不要编造。"
            )

            st.session_state.answer = answer
            st.session_state.top = top

if "answer" in st.session_state:
    st.write(st.session_state.answer)

    with st.expander("查看检索到的段落"):
        for s, i, c in st.session_state.top:
            st.markdown(f"**块 {i}（得分 {s}）**：{c}")