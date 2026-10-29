# 我的 Python / AI 速查表

> 这是我自己踩坑总结的，忘了就翻，翻三次就记住了。
> 最后更新：2026-10-24

---

## 一、运行命令

| 文件类型 | 命令 |
|---|---|
| 普通 Python 脚本 | `python 文件名.py` |
| **Streamlit 网页** | **`streamlit run app.py`** |
| 停止 Streamlit | `Ctrl + C` |

> ⚠️ `python app.py` 只会执行代码，不会启动网页服务器。

---

## 二、Python 基础语法

| 想做什么 | 写法 |
|---|---|
| 定义函数 | `def ask(question, system="默认值"):` |
| 返回值 | `return 结果` |
| 判断 | `if x in y:` / `elif` / `else:` |
| 遍历 | `for item in 列表:` |
| 带下标遍历 | `for i, item in enumerate(列表):` |
| 注释 | `# 这是注释` |
| 格式化字符串 | `f"{变量} : {另一个变量}"` |

**规则：**
- 用**缩进**表示代码块（不用 `{}`）
- 字符串必须加引号，变量不加
- 判断永远为真的条件 = 白写

---

## 三、字符串

| 想做什么 | 写法 | 结果 |
|---|---|---|
| 转小写 | `"ABC".lower()` | `"abc"` |
| 转大写 | `"abc".upper()` | `"ABC"` |
| **按任意空白切分** | `"a  b\tc".split()` | `['a','b','c']` |
| 按一个空格切分 | `"a  b".split(" ")` | `['a','','b']` |
| **用分隔符粘起来** | `"-".join(["A","B","C"])` | `"A-B-C"` |
| 取长度 | `len("abc")` | `3` |
| 去首尾空白 | `"  a  ".strip()` | `"a"` |
| 判断字母 | `"a".isalpha()` | `True` |
| 判断空白 | `" ".isspace()` | `True` |

**口诀：**
- `split()` 是「拆」，`join()` 是「粘」，互为逆操作
- `join` 的胶水写在前面：`"胶水".join(列表)`

---

## 四、列表 & 字典

### 列表（list）

| 想做什么 | 写法 | 结果 |
|---|---|---|
| 取第一个 | `nums[0]` | 第一个元素 |
| **取最后一个** | `nums[-1]` | 最后一个 |
| **取前 2 个** | `nums[:2]` | 第 0、1 个 |
| **取最后 2 个** | `nums[-2:]` | 最后两个 |
| 取下标 1 到 3 之前 | `nums[1:3]` | 第 1、2 个 |
| 追加 | `nums.append(x)` | 加到末尾 |
| 长度 | `len(nums)` | 元素个数 |
| 排序 | `sorted(nums)` | 新列表 |

**切片口诀：`[a:b]` 含头不含尾，取 `b-a` 个元素。**

```
 nums = [10, 20, 30, 40, 50]
         0   1   2   3   4
nums[:2]   = [10, 20]          ← 前两个
nums[2:5]  = [30, 40, 50]      ← 从下标2开始，到5之前
nums[-2:]  = [40, 50]          ← 最后两个
```

### 字典（dict）

| 想做什么 | 写法 |
|---|---|
| 建空字典 | `counts = {}` |
| 写入/修改 | `counts["the"] = 5` |
| **加 1** | `counts["the"] += 1` |
| 判断有没有这个键 | `"the" in counts` |
| 取值（不存在给默认） | `counts.get("the", 0)` |
| 所有键值对 | `counts.items()` |

**词频统计标准写法：**

```python
counts = {}                    # ← 必须在循环外面
for w in words:
    if w in counts:            # ← 判断字典，不是判断列表！
        counts[w] += 1         # ← 改的是"某一页"，不是整个字典
    else:
        counts[w] = 1
```

**口诀：`counts` 是笔记本，`counts["the"]` 是某一页。**

---

## 五、排序

```python
sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]
```

| 部分 | 含义 |
|---|---|
| `counts.items()` | 字典 → `[('the',5), ('fox',3)]` |
| `key=lambda x: x[1]` | 按第 2 项（次数）排 |
| `reverse=True` | 从大到小（`False` 或不写 = 从小到大） |
| `[:10]` | 取前 10 个 |

**注意：**
- `key` / `reverse` 是**关键字参数**，必须带名字
- 位置参数（要排的东西）必须在最前

---

## 六、文件读写

```python
# 读
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 写（覆盖）
with open("summary.md", "w", encoding="utf-8") as f:
    f.write(output)
```

| 模式 | 含义 |
|---|---|
| `"r"` | 读 |
| `"w"` | 写（**会覆盖原内容**） |
| `"a"` | 追加 |

- **`encoding="utf-8"` 必须写**，否则中文乱码
- **路径相对于运行命令时所在的文件夹**
- 方法名是 `read()`，不是 `reading()`

---

## 七、常见报错对照

| 报错 | 原因 | 怎么查 |
|---|---|---|
| `NameError: name 'x' is not defined` | 变量没定义 / 忘了加引号 | 看是不是把字符串当变量了 |
| `KeyError: 'the'` | 字典里没有这个键 | 是不是 `+=` 之前没初始化 |
| `IndexError: list index out of range` | 下标越界 | `len()` 看看有多少个 |
| `FileNotFoundError` | 路径不对 / 文件名拼错 | 报错里的路径是不是有变量名 |
| `AttributeError: ... has no attribute 'xxx'` | 方法名写错 | `dir(对象)` 查有哪些方法 |
| `TypeError: can only concatenate str` | 字符串和数字拼接 | 用 `str()` 转一下 |
| `SyntaxError: invalid character` | 用了中文标点（`：`、`，`） | 检查引号和冒号 |
| `ModuleNotFoundError` | 库没装 | `pip install 库名` |
| `UnboundLocalError` | 变量在函数里先用了 | 检查初始化位置 |

**看到报错先看：哪一行、什么类型、涉及什么名字。**

---

## 八、Git

```powershell
git status                    # 看状态（先跑这个！）
git add .                     # 把改动放进待提交区
git commit -m "说明"          # 提交
git push                      # 推到 GitHub
git log --oneline             # 看提交历史
```

**护身符：敲 Git 命令前，先看提示符里是不是项目目录。**

| 报错 | 原因 |
|---|---|
| `not a git repository` | 不在项目目录里，先 `cd` |
| `rejected` / `fetch first` | 建仓库时勾了 README，本地和远程冲突 |
| `Recv failure: Connection was reset` | 网络被墙，重试；或改用 SSH |

**远程地址：**

```powershell
git remote -v                                                  # 查看
git remote set-url origin git@github.com:用户名/仓库.git        # 改成 SSH
```

**SSH 配置**（`C:\Users\HUAWEI\.ssh\config`）：

```
Host github.com
    HostName ssh.github.com    ← 绕开被墙的 github.com:443
    Port 443
    User git
    IdentityFile ~/.ssh/id_ed25519
```

---

## 九、大模型 API（智谱 GLM）

```python
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
        {"role": "system", "content": "你是严格的老教授"},
        {"role": "user",   "content": "什么是人工智能？"},
    ],
)

print(resp.choices[0].message.content)
```

**关键点：**

| 项 | 说明 |
|---|---|
| `base_url` | 智谱的地址；换平台只改这里和 model |
| `messages` | **必须是列表**，即使只有一条 |
| `role` | `system` = AI 的人设，`user` = 用户的话 |
| `choices` | 候选回答列表，默认只有 1 个 |
| `[0]` | 第一个候选（只有 1 个时，`[1]` 会 IndexError） |
| `.message` | 那条消息对象（含 role 和 content） |
| `.content` | 文字内容 |

**模型代码：**
- `glm-5.3-flash` — 便宜，日常用
- `glm-5.3-flashx` — 更快
- `glm-5.3` — 旗舰，贵

**提示词技巧：**
- 规则写进 `system`，内容放进 `user`
- 用编号列规则（1. 2. 3.）
- 要它守格式，就把禁区写死：「只输出译文，不加解释、不加引号、不给多个版本」
- 想要输出稳定，加 `temperature=0`

---

## 十、Streamlit

```python
import streamlit as st

st.title("标题")
text = st.text_area("提示文字", height=150)   # 返回输入的文字
if st.button("按钮文字"):                     # 返回 True/False
    with st.spinner("处理中..."):
        result = 干活()
st.write(result)
```

**运行：`streamlit run app.py`**（不是 `python app.py`）

**`session_state` —— 跨 rerun 保存数据：**

```python
if "result" not in st.session_state:        # ① 初始化
    st.session_state.result = ""

if st.button("翻译"):
    st.session_state.result = 干活()         # ② 存进状态

if st.session_state.result:                  # ③ 每次执行都显示
    st.write(st.session_state.result)
```

**原理：每次控件交互 → 整个脚本从头重跑 → 普通变量会丢，`session_state` 不丢。**

---

## 十一、安全习惯

| 规则 | 说明 |
|---|---|
| API Key 只进 `.env` | 不进代码、不进聊天框、不进截图 |
| `.env` 必须在 `.gitignore` 里 | 否则会上传到 GitHub |
| 提交前必看 `git status` | 确认没有 `.env` |
| 公钥可以公开，私钥绝不外传 | `id_ed25519.pub` 可以发，`id_ed25519` 不行 |
| key 泄露了就删掉重建 | 不在原 key 上纠结 |

**`.env` 格式：**

```
ZHIPU_API_KEY=你的key
```

（等号两边无空格，不加引号，结尾不留空格）

---

## 十二、模块与导入

```python
# llm_utils.py
def ask(question, system="默认"):
    ...

if __name__ == "__main__":     # 只有直接运行才执行
    print(ask("测试"))

# 其他文件
from llm_utils import ask
```

**`import` 会把模块从头执行一遍**，所以测试代码要放进 `if __name__ == "__main__":`。

**文件名不能和库重名**（别叫 `openai.py`、`random.py`）。

---

## 十三、RAG 与 embedding

### 完整链路

```
读文件 → 切块 → 算向量 → 存索引 → 检索 → 喂 prompt → 回答
           检索 Retrieval    增强 Augmented    生成 Generation
```

### 算向量（embedding）

```python
r = client.embeddings.create(model="embedding-3", input="文本")
vec = r.data[0].embedding      # 2048 个浮点数
```

**意思相近的文字，向量也相近。**

### 余弦相似度

```python
import numpy as np

def cos(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))
```

| 分数 | 含义 |
|---|---|
| ≈ 1.0 | 意思几乎一样 |
| 0.6 - 0.8 | 明显相关 |
| 0.4 - 0.6 | 弱相关 |
| ≈ 0 | 无关 |

`a @ b` = 点积；`np.linalg.norm(a)` = 向量长度。除以长度 = 只看方向，不看长短。

### 建索引 + 存文件

```python
chunks = materials.split("\n\n")

r = client.embeddings.create(model="embedding-3", input=chunks)
vectors = [d.embedding for d in r.data]

with open("embeddings.json", "w", encoding="utf-8") as f:
    json.dump({"chunks": chunks, "vectors": vectors}, f, ensure_ascii=False)
```

> 批量 `input=chunks` 不支持时，改成 for 循环一个个传。
> 加了新文件必须重跑，索引不会自动更新。

### 检索

```python
with open("embeddings.json", "r", encoding="utf-8") as f:
    d = json.load(f)
chunks = d["chunks"]
vectors = [np.array(v) for v in d["vectors"]]

qv = np.array(client.embeddings.create(
    model="embedding-3", input=问题).data[0].embedding)

scored = [(cos(qv, v), i) for i, v in enumerate(vectors)]
scored.sort(reverse=True)

top = scored[:3]                              # [(分数, 下标), ...]
context = "\n\n".join([chunks[i] for s, i in top])
```

### 两种检索对比

| 方式 | 原理 | 缺点 |
|---|---|---|
| n-gram 关键词 | 字面重合 | **换个说法就找不到** |
| **embedding 向量** | 语义相似 | 要先算向量、占空间 |

**实测：问「大模型是怎么训练的」，块1（讲训练过程的）在关键词检索里排第 5（被 top_k=3 漏掉），在向量检索里排第 2。**

**结论：RAG 的效果 80% 取决于检索，不是模型。**

---

## 十四、快速回忆表

| 想干什么 | 写法 |
|---|---|
| 从大到小排序 | `sorted(x, reverse=True)` |
| 多行字符串嵌变量 | `f"""...{x}..."""` |
| 缓存函数结果 | `@st.cache_data` 写在 `def` 上一行 |
| 单行输入框 | `text = st.text_input("提示")` |
| 按钮 | `if st.button("文字"):` |
| 折叠面板 | `with st.expander("标题"):` |
| 跨重跑保存 | `st.session_state.键 = 值` |
| 存索引 | `json.dump(数据, f, ensure_ascii=False)` |
| 读索引 | `json.load(f)` |
| 转成数组 | `np.array(列表)` |
| 点积 | `a @ b` |
| 向量长度 | `np.linalg.norm(a)` |

### 运行命令（最容易忘）

| 文件里有 `import streamlit`？ | 命令 |
|---|---|
| 没有 | `python 文件名.py` |
| **有** | **`streamlit run 文件名.py`** |

**看到 `missing ScriptRunContext` → 就是用了 `python` 跑 Streamlit。**

### 环境变量排错

```
配置明明对了却不生效
  → 检查系统环境变量有没有覆盖 .env
  → [Environment]::GetEnvironmentVariable("变量名","User")
  → load_dotenv(override=True)   # 让 .env 说了算
  → 改完必须重启进程
```

---

## 十五、待学 / 待补

- [x] RAG：切块 + 检索
- [x] embedding 与向量检索
- [ ] `join` 的具体输出
- [ ] `return` vs `print` 的深入理解
- [ ] 部署 Streamlit 到公网（注意额度和密钥安全）
- [ ] 索引增量更新（加文件后自动重建）
- [ ] 用 `st.file_uploader` 让用户自己上传文档
