import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client=OpenAI(
    api_key=os.environ["ZHIPU_API_KEY"],
    base_url="https://open.bigmodel.cn/api/paas/v4/",
)
def ask(question, system="你是一个有帮助的助手"):
    resp = client.chat.completions.create(
        model="glm-5.3-flash",
        messages=[
            {"role": "system", "content": system},
            {"role": "user",   "content": question},
        ],
    )
    return resp.choices[0].message.content


if __name__ == "__main__":
    print(ask("用一句话解释什么是 Python"))