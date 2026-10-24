import os 
from llm_utils import ask

files = os.listdir("notes")
results = []  
for name in files:      
    path = os.path.join("notes", name)
    with open(path,"r",encoding="utf_8") as f:
        content=f.read()
    summary = ask(content, "你是文章总结助手。用一句话概括核心观点，不超过 40 字")
    results.append(f"## {name}\n{summary}") 
output = "\n\n".join(results)
print(output)

with open("summary.md", "w", encoding="utf-8") as f:
    f.write(output)