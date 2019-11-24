"""110 Minimum Path Sum

确认条件
# 起始点为(0, 0)
# mxn的网格内都是非负整数
# 每次移动1，方向为向下或者向右
# 求到达最右下角的最小路径

Algorithm:
1. 确认转态
dp[i][j]表示到达此坐标的最小值。最终结果为dp[i][j]

2. 状态转移方程
想要到达dp[i][j]，先要到达dp[i-1][j]和dp[i][j-1]，而最小值就在二者之间
dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

3. 初始状态和边界情况
dp[0][0] = grid[i][j]
上边和左边只有一种到达的可能性
dp[0][j] += dp[0][j-1]
dp[i][0] += dp[i-1][0]
其他情况, i>0, j>0; 运用完整的状态转移方程

4. 计算顺序
自左向右
自上而下

Note:
1. 使用一维滚动数组做了优化

Complexity:
O(m*n)

"""


class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """

    # def minPathSum(self, grid):
    #     m, n = len(grid), len(grid[0])
    #     dp = [[0 for j in range(n)] for i in range(m)]
    #     dp[0][0] = grid[0][0]

    #     for i in range(m):
    #         for j in range(n):
    #             if i == 0 and j == 0:
    #                 continue
    #             if i == 0:
    #                 dp[i][j] = dp[i][j - 1] + grid[i][j]
    #             elif j == 0:
    #                 dp[i][j] = dp[i - 1][j] + grid[i][j]
    #             else:
    #                 dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    #     print(dp)
    #     return dp[-1][-1]

    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        # 这种初始化方法可以处理i=0的情况
        dp = [0] + [sys.maxsize] * (n - 1)

        for i in range(m):
            for j in range(n):
                if j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]