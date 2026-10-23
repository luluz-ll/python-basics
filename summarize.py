import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["ZHIPU_API_KEY"],
    base_url="https://open.bigmodel.cn/api/paas/v4/",
)

# ---------------- 第 1 步：读取文件 ----------------
# TODO 1: 读取 notes.txt 的内容，存到变量 text 里
#
# 提示（三行，注意缩进）：
#   with open("notes.txt", "r", encoding="utf-8") as f:
#       text = f.read()
#
# 你必须理解的三点：
#   1. "r" 表示读取模式（read）
#   2. encoding="utf-8" 必须写，否则中文在 Windows 上会乱码
#   3. text = f.read() 要缩进，因为它要在 with 里面执行
#
# 在这里写你的代码：
with open("notes.txt","r",encoding="utf-8") as f:
    text = f.read()


# ---------------- 第 2 步：组装提问 ----------------
# TODO 2: 把 text 的内容放进 prompt 里
#
# 提示：
#   prompt = f"请用三句话总结下面的内容：\n\n{text}"
#
# 理解：
#   f"..." 让你能在字符串里嵌入变量
#   \n\n 是两个换行，用来把你写的指令和原文分开
#
# 在这里写你的代码：
prompt = f"用 1. 2. 3. 编号，列出原文的三个阶段，每条不超过 20 字 : \n\n{text}"


# ---------------- 第 3 步：调用模型（已写好，不用改）----------------
resp = client.chat.completions.create(
    model="glm-5.3-flash",
    messages=[
        {"role": "user", "content": prompt}
    ],
)

# ---------------- 第 4 步：打印结果（已写好，不用改）----------------
print(resp.choices[0].message.content)
