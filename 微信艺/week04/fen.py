Dict = {"经常":0.1,
        "经":0.05,
        "有":0.1,
        "常":0.001,
        "有意见":0.1,
        "歧":0.001,
        "意见":0.2,
        "分歧":0.2,
        "见":0.05,
        "意":0.05,
        "见分歧":0.05,
        "分":0.1}

#待切分文本
sentence = "常经有意见分歧"

#实现全切分函数，输出根据字典能够切分出的所有的切分方式
def all_cut(sentence, Dict):
    results = []  # 存储所有切分结果
    path = []  # 当前切分路径

    def backtrack(start):
        # 当切分位置到达句子末尾，将当前路径加入结果
        if start == len(sentence):
            results.append(path[:])  # 使用切片复制当前路径
            return

        # 尝试所有可能的切分长度
        for end in range(start + 1, len(sentence) + 1):
            word = sentence[start:end]  # 当前候选词
            # 如果候选词在词典中，则继续切分
            if word in Dict:
                path.append(word)  # 加入当前路径
                backtrack(end)  # 递归切分剩余部分
                path.pop()  # 回溯，移除当前词

    backtrack(0)  # 从位置0开始切分
    return results


# 测试
target = all_cut(sentence, Dict)
for seg in target:
    print(seg)