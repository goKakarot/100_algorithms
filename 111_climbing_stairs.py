"""111 Climbing Stairs

确认条件
# 起始点为0
# 终止位置在n
# 每次只能移动1或2
# 求到达n的方案总数

Algorithm:
1. 确定状态
dp[i]表示到达此楼层的方案总数。最终答案dp[n]
还需要一个数组s[]，s[i-1]记录dp[i-1]里以1结尾的方案个数。因为dp[i]不仅要包含dp[i-1]的方案
个数，dp[i-1]中以1结尾的方案再加上1后可以被归并为以2结尾的新方案
注意：这里s[i-1]的值实际上等于dp[i-2]

i = 0

i = 1
01
dp[0] = 1, s[0] = 1

i = 2
011, 02
dp[1] = 2, s[1] = 1

i = 3
0111, 012, 021
dp[2] = 3, s[2] = 2

i = 4
01111, 0121, 0211
0112,        022
dp[3] = 5

2. 状态转移方程
要获得dp[i]必须先知道dp[i-1]和s[i-1]
dp[i] = dp[i-1] + s[i-1]
or
dp[i] = dp[i-1] + dp[i-2]

3. 初始状态和边界情况
因为dp[i]依赖于前两次的状态，所以先判断n>2，n=1,2为特殊情况不能通过前面的状态获得

4. 计算顺序
从小到大

"""


class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        if n == 0:
            return 0
        if n <= 2:
            return n

        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[-1]

