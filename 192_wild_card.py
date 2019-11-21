"""192 Wild Card

Algorithm:
1. 动态规划（https://www.cnblogs.com/grandyang/p/4401196.html）
2. 着手点为：
通配符'*'可以匹配哪些字符？
ABC三种可能，以此构建状态转移方程。
注意，DP题假如有两个变量，就有两个循环，推导状态时要控制s[i]和p[j]中的一个不变
状态转移方程: s[i]能够匹配p，可以从s[i-1]能否匹配p推导得出
如何构建存储状态的数据结构？
因为有两个变量至少要用二维数组，由于'*'可以匹配空字符，所以要开辟额外一个空间给空字符

Note:
1. 注意，创建的二维数组要考虑空串的情况
s = ['' a b c]
p = ['' a * c]

2. 在推导状态转移方程时有两种情况：
其一是，p遇到通配符‘？’时，那么dp[i][j]为True，和s[i]等于p[j]归为一类
其二是，p遇到通配符‘*’时，要考虑三点：
A. '*'匹配空字符时，算是一个corner case
    s = a, p = a*
B. '*'匹配到1个字符
    s = abc, p = a*c
C. '*'匹配到n个字符
    s = abc, p = a*
实际上B是C的一个子集，区分这两种情况方便记忆
注意可以用C取代B，反之则不可以，例如，尝试把C的例子代入计算dp[i = 1][j = 1]判断条件

3. A匹配空就像是补了一位，
C第一次(ab, a*)借了A一位(空+char = *)，C第二次(abb, a*)看上一次a*时是否能匹配上，匹配上
了就再借一位(空+char+char = *)，先有A才会有C

4. 别想太复杂！！！

Complexity:
O(m * n)

"""


class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """

    def isMatch(self, s, p):
        m, n = len(s), len(p)
        # init the 2-d array to store matching states
        # dp[0][j] 代表s为空串时和j个字符的p的匹配度
        # dp[i][0] 代表i个字符的s和空字符的p的匹配度（除了s = ''，其他False）
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # 空串对空串
        dp[0][0] = True

        # init: '*' match any sequence of characters(including empty sequence)
        # s = ''时，s和p能否匹配
        # p = *，dp[0] = [True, True]
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # i从1循环，因为要判断之前的状态，i从0开始会数组越界
        for i in range(1, m + 1):
            # j也从1开始循环，j = 0表示p为空串状态，因为都是False不需要处理
            # dp[i][j]代表的是s[i]p[j-1]的状态，错开了一位
            # dp[i][j]  0  1  2  3
            #           '' a  *  c
            # p[j]      a  *  c
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    #           匹配0个           匹配1个             匹配n*个
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j - 1] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (
                            s[i - 1] == p[j - 1] or p[j - 1] == '?')

        return dp[m][n]

