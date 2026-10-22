# python-basics

我的 Python 练习项目。从零开始，边写边学。

## wordcount.py

统计一段文本中每个单词出现的频率，按次数从高到低输出前 10 名。

### 实现思路

1. 把文本统一转成小写（避免 `The` 和 `the` 被算成两个词）
2. 遍历每个字符，只保留字母和空白字符，过滤掉标点
3. 用 `split()` 按空白切分成单词列表
4. 用字典（dict）统计每个单词出现的次数
5. 用 `sorted()` + `lambda` 按次数降序排序，切片取前 10 个

### 运行

```bash
python wordcount.py
```

### 示例输出

```
the : 5
fox : 3
dog : 3
quick : 2
brown : 2
jumps : 2
over : 2
lazy : 2
barks : 1
and : 1
```

## practice.py

Python 语法速览，写给有 C 基础的人。包含 12 个最小片段：变量、字符串、
列表、字典、循环、字符判断、排序等。

### 运行

```bash
python practice.py
```
