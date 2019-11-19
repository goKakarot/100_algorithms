"""683 word break iii

Algorithm:
1. 和word-break i的思路是一样的，用DP来做

Note:
1. 详见注释

Complexity:
O(n^2)

"""


class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # 0     s = 'something' dict = ''
        # x     s = ''          dict = 'something'
        # x     s = ''          dict = ''
        # 这题对临界情况的判断并不做详细要求
        # 情况2实际上会报错
        if len(dict) == 0:
            return 0

        lower_dict = set()
        for word in dict:
            # dict和set型的添加是使用add
            lower_dict.add(word.lower())

        n = len(s)
        max_value = max([len(w) for w in dict])
        # 注意这种写法
        res = [0 for _ in range(n + 1)]
        res[0] = 1
        for i in range(1, n + 1):
            for j in range(1, min(i, max_value) + 1):
                if res[i - j] == 0:
                    continue
                if s[i - j:i].lower() in lower_dict:
                    # 需要累加上之前的可行性
                    res[i] += res[i - j]
                    # 这里不需要break，因为要考虑所有的情况
        return res[-1]

