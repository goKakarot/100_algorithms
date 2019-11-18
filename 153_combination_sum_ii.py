"""153 Combination Sum II

Algorithm:
1. 首先要排序，这样可以控制搜索的顺序。但是这时不能将num里重复的数字去除，因为题目要求每个数
字都要使用一次。
2. 由于结果不能有重复，考虑一个例子：[2, 2, 3]。按照dfs，我们从第一个2开始做搜索，也要从第
二个2开始做搜索。这样会导致重复。所以在dfs中，如果选择从某个数"开始"，如果后面有重复的数，就
必须要跳过，因为搜索的结果会重复

Note:
1. 首先要记得排序
1. 这里比较麻烦的是去重，我使用了use这个变量，它的作用是在向后查找时比较前一个数字是否作为过
搜索的起始位置

"""


class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        curr_val, curr_comb, use, index = 0, [], [0]*len(num), 0
        self.result = []
        num.sort()
        self.dfs(num, target, curr_val, curr_comb, use, index)
        return self.result

    def dfs(self, num, target, curr_val, curr_comb, use, index):
        if curr_val == target:
            self.result.append(curr_comb[:])
            return

        for i in range(index, len(num)):
            if curr_val < target and (i == 0 or num[i-1] != num[i] or use[i-1] == 1):
                use[i] = 1
                curr_comb.append(num[i])
                self.dfs(num, target, curr_val+num[i], curr_comb, use, i+1)
                curr_comb.pop()
                use[i] = 0


# let write some test cases
sol = Solution()
num = [7, 1, 2, 5, 1, 6, 10]
target = 8

print(sol.combinationSum2(num, target))