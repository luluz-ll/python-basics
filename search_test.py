import json
import numpy as np
from llm_utils import client

# 1. 加载索引
with open("embeddings.json", "r", encoding="utf-8") as f:
    data = json.load(f)

chunks = data["chunks"]
vectors = [np.array(v) for v in data["vectors"]]


# 2. 余弦相似度
def cos(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))


# 3. 把问题变向量
question = "大模型是怎么训练的"
r = client.embeddings.create(model="embedding-3", input=question)
qv = np.array(r.data[0].embedding)

# 4. 跟每一块比，排序
scored = []
for i, v in enumerate(vectors):
    scored.append((cos(qv, v), i))

scored.sort(reverse=True)

# 5. 打印前 5
print("问题:", question)
print()
for s, i in scored[:5]:
    print(f"{s:.4f}  块{i}: {chunks[i][:35]}...")