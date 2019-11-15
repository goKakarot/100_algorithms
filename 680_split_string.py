"""680 Split String

Algorithm
1. 是求所有子集问题的简化版，只要求出1和2个字符串组合子集的问题
2. Solution2是Solution的初始版本，1把2写进了循环。1是每次递归移动s，2是每次index+1

"""


class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """
    def splitString(self, s):
        result, path = [], []
        self.dfs(result, path, s)
        return result

    # result: 不断增加的数组个数
    # path：单次递归保留的数组结果
    # s：字符串
    def dfs(self, result, path, s):
        if s == '':
            # 只用path是浅拷贝，
            # 所以最开始append进results里面的path会因为path赋值的改变而改变。
            # 所以我们需要clone深拷贝
            result.append(path[:])
            return

        for i in range(2):
            if i+1 <= len(s):
                path.append(s[:i+1])
                self.dfs(result, path, s[i+1:])
                path.pop()


class Solution2:
    """
    @param: : a string to be split
    @return: all possible split string array
    """
    def splitString(self, s):
        result, path = [], []
        index = 0
        self.dfs(result, path, s, index)
        return result

    # result: 不断增加的数组个数
    # path：单次递归保留的数组结果
    # s：字符串
    def dfs(self, result, path, s, index):
        if index == len(s):
            result.append(path[:])
            return

        path.append(s[index])
        self.dfs(result, path, s, index+1)
        path.pop()

        # 数组有越界可能性!
        if index+2 <= len(s):
            path.append(s[index:index+2])
            self.dfs(result, path, s, index+2)
            path.pop()

        """
        for i in range(2):
            if index+i <= len(s):
                path.append(s[index:index+i+1])
                self.dfs(result, path, s, index+i+1)
                path.pop()
        """

