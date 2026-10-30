# 运行方式：streamlit run rag_app.py
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


# ---------- 3. 批量算向量 ----------
def embed_texts(texts):
    r = client.embeddings.create(model="embedding-3", input=texts)
    return [np.array(d.embedding) for d in r.data]


# ---------- 4. 检索 ----------
def retrieve(question, vectors, top_k=3):
    r = client.embeddings.create(model="embedding-3", input=question)
    qv = np.array(r.data[0].embedding)

    scored = []
    for i, v in enumerate(vectors):
        scored.append((cos(qv, v), i))

    scored.sort(reverse=True)
    return scored[:top_k]


# ---------- 5. 读取上传的文件 ----------
def read_uploaded(uploaded):
    """从上传的文件里提取纯文本。支持 .txt 和 .docx。"""
    name = uploaded.name.lower()

    if name.endswith(".docx"):
        from docx import Document
        doc = Document(uploaded)
        # 跳过空段落
        paras = [p.text for p in doc.paragraphs if p.text.strip()]
        return "\n\n".join(paras)

    # 其他按纯文本读
    return uploaded.read().decode("utf-8", errors="ignore")


# ---------- 页面 ----------
st.title("我的知识库问答")

uploaded = st.file_uploader(
    "上传 txt 或 docx 文件（不传就用内置笔记）",
    type=["txt", "docx"],
)

# 决定用哪套资料
if uploaded is not None:
    key = f"{uploaded.name}-{uploaded.size}"

    # 只有换了新文件才重新算向量（避免每次重跑都调用 API）
    if st.session_state.get("file_key") != key:
        with st.spinner("正在处理上传的文件..."):
            text = read_uploaded(uploaded)

            if not text.strip():
                st.error("这个文件里没有读到文字（可能是扫描件或只有图片）。")
                st.stop()

            chunks = [c for c in text.split("\n\n") if c.strip()]
            vectors = embed_texts(chunks)

            st.session_state.file_key = key
            st.session_state.file_chunks = chunks
            st.session_state.file_vectors = vectors

    chunks = st.session_state.file_chunks
    vectors = st.session_state.file_vectors
    source = f"上传的文件：{uploaded.name}"
else:
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

            st.session_state.answer = answer
            st.session_state.top = top
            st.session_state.used_chunks = chunks

if "answer" in st.session_state:
    st.write(st.session_state.answer)

    with st.expander("查看检索到的段落"):
        for s, i in st.session_state.top:
            st.markdown(
                f"**块 {i}（相似度 {s:.4f}）**：{st.session_state.used_chunks[i]}"
            )
