import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["ZHIPU_API_KEY"],
    base_url="https://open.bigmodel.cn/api/paas/v4/",
)

resp = client.chat.completions.create(
    model="glm-5.3-flash",
    messages=[
        {"role": "system", "content": "你是一个会指出错误的老教授"},
        {"role": "user", "content": "用一句话解释什么是 Python"}
    ],
)

print(resp.choices[0].message.content)