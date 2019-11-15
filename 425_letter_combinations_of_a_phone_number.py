"""425 Letter Combination of a Phone Number

Algorithm:
1. 这是道很典型的dfs，和680十分相似，最大不同之处我认为就是这道没有数组越界的检查。
2. 最直观的思路就是遍历digits，对每一个char对应的都加入到最后的结果
3. 直接for循环代码不好写，所以使用dfs递归，用path保留每次dfs的搜索结果

Note:
1. 注意，在7和9的位置上是四个字符，假如使用680的做法那么应该循环几次？一个小技巧是把每个数字
对应的字符串写进KEYBOARD这样的一个dict内，这样的好处是可以进行定制化的存取，直接循环每个
字符串而不需要对7和9这两个特例进行检查。

Complexity:
O(mn)
m - digits长度
n - 每个char对应的编码长度

"""


KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if not digits:
            return []

        result, path = [], ''
        index = 0
        self.dfs(result, path, digits, index)
        return result

    def dfs(self, result, path, digits, index):
        if index == len(digits):
            result.append(path[:])
            return

        for letter in KEYBOARD[digits[index]]:
            path += letter
            self.dfs(result, path, digits, index+1)
            path = path[:-1]

        """
        for letter in KEYBOARD[digits[index]]:
            self.dfs(result, path+letter, digits, index+1)
        """
