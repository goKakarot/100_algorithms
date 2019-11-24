"""114 Unique Paths

确认条件：
# 起始点在网格的左上角
# 每次只能向下或者向右移动一次
# 终止位置在右下角
# 求多少种解法

Algorithm：
1. 确认状态
dp[i][j]表示到达此坐标的方案总数。dp[m-1][n-1]是最终答案

2. 状态转移方程
想要到达dp[i][j]，先要到dp[i-1][j]或者dp[i][j-1]
dp[i][j] = dp[i-1][j] + dp[i]][j-1]

3. 初始状态和边界情况
dp[0][j]和dp[i][0]都初始化为1，因为上边和左边只有一种到达方案

4. 计算顺序
从上到下，从左到右

"""

class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

