"""94 Balanced Binary Tree

Algorithm:
分治
平衡就返回子树高度，不平衡返回-1

Note:
递归地特点是，只需要设身处地得考虑当前节点的所有子情况

"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def __init__(self):
        self.not_balanced = -1

    def is_balanced(self, root):
        return self.max_depth(root) != self.not_balanced

    def max_depth(self, root):
        if not root:
            return 0

        left = self.max_depth(root.left)
        right = self.max_depth(root.right)

        # 左右子树有任意一个不是平衡二叉树
        if left == self.not_balanced or right == self.not_balanced:
            return self.not_balanced

        # 判断当前节点是不是平衡的
        if abs(left - right) > 1:
            return self.not_balanced

        # 平衡的话返回当前节点的高度
        return max(left, right) + 1

