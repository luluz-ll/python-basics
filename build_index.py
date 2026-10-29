import os
import json
from llm_utils import client

# 1. 读文件 + 切块
files = os.listdir("notes")
all_texts = []
for name in files:
    path = os.path.join("notes", name)
    with open(path, "r", encoding="utf-8") as f:
        all_texts.append(f.read())

chunks = "\n\n".join(all_texts).split("\n\n")
print("块数:", len(chunks))

# 2. 批量算向量
r = client.embeddings.create(model="embedding-3", input=chunks)
vectors = [d.embedding for d in r.data]
print("向量数:", len(vectors), "维度:", len(vectors[0]))

# 3. 存成文件
with open("embeddings.json", "w", encoding="utf-8") as f:
    json.dump({"chunks": chunks, "vectors": vectors}, f, ensure_ascii=False)

print("已保存到 embeddings.json")