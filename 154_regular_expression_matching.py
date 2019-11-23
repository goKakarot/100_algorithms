"""154 Regular Expression Matching

Algorithm:
1. 192通配符很类似，可以套用模板。
但是不同的是对于'*'的处理，通配符的'*'可以代替任意字符，而正则表达式的'*'表示的是之前的字符
可以有0个，1个甚至n个。就是说，字符串a*b，可以表示b或是abbb，即a的任意个数。这题没有通配符那么
容易思考，因为'*'的状态是跟前一个字符捆绑的。

Note:
1. 分三种情况思考
首先是常规匹配的场景:
dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
然后就是'*'的场景了:
A. 匹配0个字符
dp[i][j] = p[j-1] == '*' and dp[i][j-2]
B. 匹配1个字符
dp[i][j] = p[j-1] == '*' and dp[i-1][j-1] and s[i-1] == p[j-2]
C. 匹配n个字符
dp[i][j] = p[j-1] == '*' and dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.')

三者是或的关系: A or B or C

2. 这个做法遗漏了'**'的情况，我们默认规则为'*'和字符时成对出现的，这会导致下面的情况:
s = aa*b
p = .**b
返回值为false，答案为true。但是lintcode没检测出来，递归没有这个问题。

Complexity:
O(m * n)

"""


class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            # 'a*b*c*'这种情况是完全可以匹配空串的
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # j是跟着dp数组走的，
                # dp数组size比p的size大一，因为dp包含了记录的空串的状态
                # 所以j - 1才能匹配p数组的位置
                if p[j - 1] == '*':
                    # A. 匹配0个字符
                    # s = 'a', p = 'ab*'
                    dp[i][j] = dp[i][j - 2]
                    # B. 匹配1个
                    # s = 'ab', p = 'ab*'
                    # dp[i][j - 1] == True and s[i - 1] == p[j - 2]
                    # C. 匹配n个
                    # s = 'abb',  p = 'ab*'     当前s等于前一个p字符    前一个p字符为'.'
                    # dp[i - 1][j] == True and (s[i - 1] == p[j - 2] or p[j - 2] == '.')
                    # 因为B为C的子集，所以只写C的情况
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        # A, B和C为或的关系
                        dp[i][j] |= dp[i - 1][j]
                else:
                    # 常规匹配
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]

