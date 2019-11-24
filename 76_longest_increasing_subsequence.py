"""76 Longest Increasing Subsequence

确定条件:
# 从一个整数序列中找到最长的升序子序列
# 子序列(sub-sequence)指的是不一定连续的n个字符
# 子串(sub-array)指的是连续的n个字符

Algorithm:
1. 确定状态
dp[i]表示以nums[i]结尾的最长子序列的长度。最终结果就是dp[n]。

2. 状态转移方程
dp的惯性思维是，要求dp[i]就必须知道dp[i-1]的最长子序列是多少？X这是错误的思路。
试想假如dp[i] = dp[i-1](nums[i] > nums[i-1]) + 1的话，以下例子就不成立:
10,11,12,1,2,3,4,5,6

这里思考的关键是dp[i]是以nums[i]结尾的最长子序列，不一定和dp[i-1]有关，而是和dp[i]之前的
所有结果有关。
处理数组型DP问题，一个最大的特点是dp[i]总是和当前值num[i]密切相关(以num[i]结尾)。或者说，
任何时刻取出dp[i]，dp[i]就是nums[i]的答案，一定要抓住这点思考转移方程的推导。
这样我们就可以推导出转移方程:
dp[i] = max{dp[0]....dp[j]} + 1 where j <= i and nums[i] > nums[j]


3. 初始状态和边界情况
首先，应该初始化dp中的每一个元素为1，因为最小的子序列总是1，即包含自己nums[i]的情况

4. 计算顺序
自左向右

Note:
1. https://blog.csdn.net/lxt_Lucia/article/details/81206439

Complexity:
O(n^2)
二分查找的时间复杂度是O(nlogn)

"""


class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)

