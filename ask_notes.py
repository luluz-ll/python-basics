import os

files = os.listdir("notes")
all_texts = []

for name in files:
    path = os.path.join("notes", name)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    all_texts.append(content)

materials = "\n\n".join(all_texts)

from llm_utils import ask

question = "红烧肉怎么做？"

prompt = f"""请根据下面的资料回答问题。
如果资料里没有答案，就回答"资料中没有相关内容"。

资料：
{materials}

问题：{question}"""

answer = ask(
    prompt,
    "你是一个基于资料回答问题的助手。只根据资料回答，不要编造。"
)

print()
print("=== 回答 ===")
print(answer)