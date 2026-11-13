import os
from llm_utils import ask

texts = []
for name in os.listdir("notes"):
    path = os.path.join("notes", name)
    with open(path, "r", encoding="utf-8") as f:
        texts.append(f.read())

materials = "\n\n".join(texts)

chunks = materials.split("\n\n")
print("切成了", len(chunks), "块")
question = "大模型是怎么训练的"
scored = []
for i, chunk in enumerate(chunks):
    hit = 0
    for j in range(len(question) - 1):
        if question[j:j+2] in chunk:
            hit += 1
    scored.append((hit, i))

scored.sort(reverse=True)

print("=== 得分前 5 名 ===")
for s, i in scored[:5]:
    print(f"  得分 {s}  块{i}: {chunks[i][:30]}...")

selected = []
for score, i in scored[:5]:
    selected.append(chunks[i])

context = "\n\n".join(selected)

prompt = f"只根据下面的资料回答问题：\n\n{context}\n\n问题：{question}"

print(ask(prompt, "只根据资料回答，不要编造"))
