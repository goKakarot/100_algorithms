"""97 Maximum Depth of Binary Tree
Algorithm:
# 遍历
自上而下的遍历
# 分治
自底而上的遍历

Note:
两种方法都是递归，区别在于函数起始的终止条件以及返回值
分治法从上到下找到最底层再从此开始向上遍历，需要返回值
遍历每层遍历临时变量比较得出最终结果交由全局变量保管，判断到触底了就可以直接返回了

Complexity:
O(N)
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def __init__(self):
        self.depth = 1

    def max_depth(self, root):
        if not root:
            return 0
        self.traverse(root, self.depth)
        return self.depth

    def traverse(self, curr_node, curr_depth):
        if not curr_node:
            return
        self.depth = max(self.depth, curr_depth)
        self.traverse(curr_node.left, curr_depth + 1)
        self.traverse(curr_node.right, curr_depth + 1)
        # still fit
        # self.depth = max(self.depth, curr_depth)

    def divide_conquer(self, root):
        if not root:
            return 0
        left = self.divide_conquer(root.left)
        right = self.divide_conquer(root.right)
        return max(left, right) + 1

