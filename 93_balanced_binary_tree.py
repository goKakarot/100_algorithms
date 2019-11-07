"""94 Balanced Binary Tree

Algorithm:
分治
显然该用分治做，注意：任何一边不平衡则直接返回

Complexity:
O(n)

"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        balanced, _ = self.validate(root)
        return balanced

    def validate(self, node):
        if node is None:
            return True, 0

        l_balanced, left = self.validate(node.left)
        if not l_balanced:
            return False, 0

        r_balanced, right = self.validate(node.right)
        if not r_balanced:
            return False, 0

        return abs(left - right) <= 1, max(left, right) + 1

