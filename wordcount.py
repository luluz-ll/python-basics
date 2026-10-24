# wordcount.py
# 目标：统计文本中每个单词出现的次数，按次数从高到低打印前 10 名
# 要求：全部代码写完不超过 20 行

def main():
    text = """
    The quick brown fox jumps over the lazy dog.
    The dog barks, and the fox runs away.
    A quick brown dog jumps over the lazy fox.
    """

    # TODO 1: 把 text 全部转成小写
    # 提示: text.lower()
    # 在这里写你的代码：
    text=text.lower()
    

    # TODO 2: 去掉标点和换行，只保留字母和空格
    # 提示: 用 for 循环遍历每个字符，只留下 c.isalpha() 或 c.isspace() 的字符
    #       把保留下来的字符拼成一个新字符串
    # 在这里写你的代码：
    new_s=""
    for c in text:
        if c.isalpha()or c.isspace():
            new_s+=c
    


    # TODO 3: 按空格切分成单词列表
    # 提示: .split()
    # 在这里写你的代码：
    words = new_s.split()
    

    # TODO 4: 用 dict 统计每个单词出现次数
    # 提示: 遍历列表，if word in counts: counts[word] += 1
    #                       else: counts[word] = 1
    # 在这里写你的代码：
    count = {}
    for c in words:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
        
    



    # TODO 5: 按次数从高到低排序，取前 10 个
    # 提示: sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]
    # 在这里写你的代码：
    top10 = sorted(count.items(), key=lambda x: x[1], reverse=True)[:10]
   

    # TODO 6: 打印，格式：单词 : 次数
    # 在这里写你的代码：
    for word, count in top10:
        print(f"{word} : {count}")


if __name__ == "__main__":
    main()
