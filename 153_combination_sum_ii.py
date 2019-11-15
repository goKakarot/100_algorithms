"""153 Combination Sum II

Algorithm:
1. 使用回溯法搜集所有可能性，是典型的for循环嵌套dfs

Note:
1. 这里比较麻烦的是去重，我使用了use这个变量它的作用是在向后查找时比较前一个数字是否进行过
搜索

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