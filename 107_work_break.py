"""107 Word-break

Algorithm:
1. 经典的DP题目，状态转移方程为：
f(i) = f(i-j) is true + s[i-j:i] in dict
这里j为dict中最长的子串长度，在i的位置向前找寻不可能超过这个len(j)

Note:
1. 用到了一些小trick，详见代码内注释

Complexity:
O(n^2)

"""


class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, dict):
        # True  s ['']          dict ['']
        # True  s ['']          dict ['something']  <== res[0] = True
        # False s ['something'] dict ['']
        # s和dict的组合只有这三种特殊情况，而代码可以处理情况2；
        # 剩下两种情况的共同点在于dict都为空
        if len(dict) == 0:
            return len(s) == 0

        n = len(s)
        # 在开辟数组时要多算上一位，假设s = lintcode, dict = ['lint', 'code']
        # 0 1 2 3 4 5 6 7 8
        # l i n t c o d e
        # T F F F T F F F T <== 用每个词的最后一位做判断
        res = [False] * (n + 1)
        # max_word = max([4, 4])
        # max_word = 4
        max_word = max([len(w) for w in dict])

        res[0] = True
        # n已经等于8，但我们还是要+1。
        # 原因上面说过了，有效操作都是在单词首位做的，即:l,c,(n+1)
        for i in range(1, n + 1):
            for j in range(1, min(i, max_word) + 1):
                # 第一个条件：f[i-j] is True 才能继续
                if not res[i - j]:
                    continue
                # 第二个条件：s[i-j:i] in dict
                # 此时n+1的好处也显示了出来，因为切片操作是前闭后开
                if s[i - j:i] in dict:
                    # 这是有效操作，i总是设置在单词首位或者n+1的坐标
                    res[i] = True
                    break
        # 也可返回res[n] = res[8]
        return res[-1]

