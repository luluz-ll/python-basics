import numpy as np
from llm_utils import client

r = client.embeddings.create(model="embedding-3", input="人工智能")
vec = r.data[0].embedding

print("维度:", len(vec))
print("前5个:", [round(x, 4) for x in vec[:5]])

def embed(text):
    r = client.embeddings.create(model="embedding-3", input=text)
    return np.array(r.data[0].embedding)


def cos(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))


a = embed("大模型是怎么训练的")
b1 = embed("把文本收集起来，让模型反复猜下一个词，猜错了调整参数")
b2 = embed("今天天气很好，我们去图书馆吧")

print("相关:", round(cos(a, b1), 4))
print("无关:", round(cos(a, b2), 4))