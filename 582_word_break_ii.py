"""582 Word Break III

Algorithm:
1. 分治（递归）+ 记忆化，dfs搜索的剪枝题
2. 基本思想是：把s拆分成prefix = s[:i]和s[i:]，如果s[:i]在dict中，那么看看s[:i]中有多少种拆分的
可能，每次循环和上一次的s[:i]合并成一个结果
3. 需要用memo来记录做过的结果，比如li+ne+code和lint+code，code被处理了两遍。
用一个hashset来表示memo，遇到重复的s[i:]就返回memo中的结果

Note:
1. 注意最后的一个判断：假如dict = ['lintcode']，sub_partitions就为[]，这时要把prefix
整个加到结果中去

Complexity:
O(n) * (O(n) + O(m)) = O(n * n) + O(n * m) = O(n * m) or O(n * n)
n = len(s)
m = number of dict

"""


class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        memo = dict()
        return self.dfs(s, wordDict, memo)

    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]

        if len(s) == 0:
            return []

        partitions = []
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue
            sub_partitions = self.dfs(s[i:], wordDict, memo)
            for partition in sub_partitions:
                partitions.append(s[:i] + ' ' + partition)

        if s in wordDict:
            partitions.append(s)

        memo[s] = partitions
        return partitions

