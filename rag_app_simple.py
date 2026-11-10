# 运行方式：streamlit run rag_app_simple.py
# 这是 rag_app.py 的瘦身版（67 行），去掉了上传功能，用来学习理解
import json
import numpy as np
import streamlit as st
from llm_utils import client, ask


# ---------- 1. 加载预建索引 ----------
@st.cache_data
def load_index():
    with open("embeddings.json", "r", encoding="utf-8") as f:
        d = json.load(f)
    return d["chunks"], [np.array(v) for v in d["vectors"]]


# ---------- 2. 余弦相似度 ----------
def cos(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))

# ---------- 4. 检索 ----------
def retrieve(question, vectors, top_k=3):
    r = client.embeddings.create(model="embedding-3", input=question)
    qv = np.array(r.data[0].embedding)

    scored = []
    for i, v in enumerate(vectors):
        scored.append((cos(qv, v), i))

    scored.sort(reverse=True)
    return scored[:top_k]

# ---------- 页面 ----------
st.title("我的知识库问答")

# 决定用哪套资料
chunks, vectors = load_index()
source = "内置笔记 notes/"
st.caption(f"知识库共 {len(chunks)} 个段落（{source}）")

question = st.text_input("问点问题")

if st.button("提问"):
    if not question.strip():
        st.warning("请先输入问题")
    else:
        with st.spinner("检索并思考中..."):
            top = retrieve(question, vectors, top_k=3)
            context = "\n\n".join([chunks[i] for s, i in top])

            prompt = f"""请根据下面的资料回答问题。

如果资料里没有答案，就回答"资料中没有相关内容"。

资料：
{context}

问题：{question}"""

            answer = ask(
                prompt,
                "你是一个基于资料回答问题的助手。只根据资料回答，不要编造。"
            )
            answer = ask(
                prompt,
                "你是一个基于资料回答问题的助手。只根据资料回答，不要编造。"
            )

            st.session_state.answer = answer      

if "answer" in st.session_state:
    st.write(st.session_state.answer)