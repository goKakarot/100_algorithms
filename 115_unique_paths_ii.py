"""115 Unique Paths II

确认条件
# 求解法总数
# 包含障碍物，是114的follow-up
# 机器人只能向下或向右走（全向走动得用搜索）
# 异常值处理（左上角，右下角为障碍的情况）

Algorithm:
1. 确认状态
dp[i][j]表示可以到达此坐标的方案总数。最终答案为dp[m-1][n-1]

2. 转移方程
想要到达dp[i][j]，先要到达dp[i-1][j]和dp[i][j-1]
dp[i][j] = dp[i-1][j] + dp[i][j-1]

为了简化书写，可以把转移方程拆开成两部分：
dp[i][j] += dp[i-1][j] and dp[i][j] += dp[i][j-1]
加上判断条件，就可以在正常的情况下刚好把第一行，第一列的初始化融合进来

这是比较难想到的优化，也可以分成三种情况i=0;j=0;i,j>0讨论分别处理

3. 初始状态和边界情况
(A)首先初始化dp[0][0]为1，obstacleGrid[0][0]为1则直接返回0
(B)对于第一行和第一列，在遇到障碍物之前，初始化为1，但从第一个障碍物之后，之后的所有位置都无
法到达，应该置为0
(C)任何位置遇到障碍物，直接赋值0
(D)对于其他位置，运用完整的状态转移方程

4. 计算顺序
从左到右，从上到下

"""


class Solution_Opt:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]

        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                # 隐含j==0
                # 顺带剔除dp[0][0]
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                # 隐含i==0
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]


class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        dp = obstacleGrid
        if dp[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if i == 0  and j == 0:
                    continue
                if dp[i][j] == 1:
                    dp[i][j] = 0
                    continue
                # 初始化第一行
                if i == 0:
                    dp[i][j] = dp[i][j - 1]
                # 初始化第一列
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                # 执行完整的转移方程
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(dp)
        return dp[-1][-1]
