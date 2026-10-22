# practice.py —— 给 C 程序员的 Python 30 分钟速览
# 运行方式：在终端里执行   python practice.py
# 不用背，跑一遍、看输出、对照注释，就够了。

# ---------- 1. 变量不用声明类型 ----------
x = 10
name = "鲸鱼娘"
print("1:", x, name, type(x))

# ---------- 2. 字符串自带方法 ----------
s = "Hello World"
print("2:", s.lower(), "|", s.upper(), "|", len(s))

# ---------- 3. 字符串不可变（和 C 不一样！）----------
s2 = s.lower()
print("3: 原值 =", s, "| 新值 =", s2)
# s.lower() 不会改 s 本身，而是"返回一个新字符串"

# ---------- 4. f-string 格式化（比 printf 舒服）----------
age = 19
print(f"4: 我今年 {age} 岁，两年后 {age + 2} 岁")
# 字符串前面加 f，{} 里可以直接写变量或表达式

# ---------- 5. list：类似数组，但能自动变长 ----------
nums = [3, 1, 2]
nums.append(5)          # 追加，不用 realloc
print("5:", nums, "| 长度 =", len(nums), "| 第一个 =", nums[0])

# ---------- 6. dict：哈希表，C 里要手写的那种 ----------
counts = {}
counts["fox"] = 1
counts["fox"] += 1      # 出现第二次
counts["dog"] = 1
print("6:", counts, "| fox 出现", counts["fox"], "次")

# ---------- 7. for 循环 = 遍历，不是计数 ----------
for n in nums:
    print("7: 元素 =", n)

# ---------- 8. 需要下标时用 enumerate ----------
for i, n in enumerate(nums):
    print("8: 下标", i, "值", n)

# ---------- 9. 字符判断（TODO 2 要用的）----------
print("9:", "a".isalpha(), "空格".isspace(), "!".isalpha())
# 字母 -> True ; 空格 -> True ; 标点 ! -> False

# ---------- 10. 字符串拼接（TODO 2 的完整逻辑）----------
out = ""
for ch in "ab!c d.":
    if ch.isalpha() or ch.isspace():
        out += ch
print("10:", repr(out))
# repr() 会把空格、换行原样显示出来（用引号包住）

# ---------- 11. 条件判断 ----------
n = 5
if n > 3:
    print("11: 大于 3")
elif n == 3:
    print("11: 等于 3")
else:
    print("11: 小于 3")
# 没有括号，冒号不能少

# ---------- 12. 排序 + lambda（TODO 5 要用的）----------
items = [("fox", 3), ("dog", 5), ("cat", 1)]
result = sorted(items, key=lambda p: p[1], reverse=True)
print("12:", result)
# key=lambda p: p[1] 的意思是：按每个元素的第 2 项（次数）排序
# reverse=True 表示从大到小

print("\n全部跑完。看懂 7、9、10 三个，你就能做完 wordcount。")
