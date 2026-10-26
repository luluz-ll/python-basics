import os
from llm_utils import ask

# ---------- 1. 读取所有文件 ----------
files = os.listdir("notes")
all_texts = []

for name in files:
    path = os.path.join("notes", name)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    all_texts.append(content)

materials = "\n\n".join(all_texts)

# ---------- 2. 切块 ----------
chunks = materials.split("\n\n")
print("切成了", len(chunks), "块")

# ---------- 3. 问题 + 去停用词 ----------
question = "大模型为什么会涌现"

STOP_WORDS = ["为什么", "什么", "怎么", "如何", "哪些", "是否", "的", "了", "是"]

def clean_question(q):
    for w in STOP_WORDS:
        q = q.replace(w, "")
    return q

q = clean_question(question)
print("清洗后的问题:", q)

# ---------- 4. 打分 ----------
def score(chunk, question):
    hit = 0
    for i in range(len(question) - 1):
        gram = question[i:i+2]
        if gram in chunk:
            hit += 1
    return hit

scored = []
for i, c in enumerate(chunks):
    s = score(c, q)
    scored.append((s, i, c))

scored.sort(reverse=True)

print("\n=== 检索结果 ===")
for s, i, c in scored[:5]:
    print(f"块{i} 得分{s}: {c[:40]}...")

# ---------- 5. 取前 3 块 ----------
top_chunks = []
for s, i, c in scored[:3]:
    if s > 0:
        top_chunks.append(c)

context = "\n\n".join(top_chunks)
print(f"\n用了 {len(top_chunks)} 块，共 {len(context)} 字")

# ---------- 6. 组装 prompt ----------
prompt = f"""请根据下面的资料回答问题。
如果资料里没有答案，就回答"资料中没有相关内容"。

资料：
{context}

问题：{question}"""

answer = ask(
    prompt,
    "你是一个基于资料回答问题的助手。只根据资料回答，不要编造。"
)

print()
print("=== 回答 ===")
print(answer)