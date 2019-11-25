"""603 Largest Divisible Subset

确定条件
# 无重复正整数集合，找出其中的最大子集，满足子集中任意两个元素都是可被整除的
# 和76同一思路，可以用模板

Algorithm:
1. 确定状态
dp[i]表示以nums[i]结尾的最大可被整除子集，
由于不仅要求是否存在子集，还要列出子集内的所有元素，所以再创建一个额外数组s[i]表示以nums[i]
结尾的子集的所有元素

2. 状态转移方程
dp[i] = max{dp[0].....dp[j]} + 1 where j <= i and nums[i] % nums[j] = 0
每次循环内，s[i]插入nums[j]

3. 初始状态和边界情况
如果是第一次匹配到字符，通过判断s[i]的值可以知道是否为第一次，那么dp[i]赋值为2，同时s[i]插
入两个字符
注意，假如不存在成对子集，那么输出第一个元素

4. 计算顺序
自左向右

Note:
1. 因为时间原因，这题要重新思考

"""


class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset
    """
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        dp = [[] for _ in range(n)]

        nums.sort()
        for i in range(n):
            for j in range(i):
                if (nums[i] % nums[j]) == 0:
                    if not dp[i]:
                        dp[i].append(nums[j])
                        dp[i].append(nums[i])
                    else:
                        # append返回值为None！
                        # list + list则有返回值
                        if len(dp[j]+[nums[i]]) > len(dp[i]):
                            dp[i] = dp[j]+[nums[i]]

        # max 返回值为dp中子数组内元素和的最大
        # 改为循环
        print(dp)
        if not max(dp):
            return [nums[0]]
        res = dp[0]
        for i in range(1, n):
            if len(dp[i]) > len(res):
                res = dp[i]

        return res

