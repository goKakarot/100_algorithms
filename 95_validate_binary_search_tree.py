"""95 Validate Binary Search Tree

Algorithm:
1. 二叉搜索树的中枢遍历结果是升序的
2. 分治法
左、右子树都为二叉搜索树
左子树的最大值小于当前节点
右子树的最小值大于当前节点
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def __init__(self):
        self.last_node = None
        self.valid = True

    def is_valid_bst(self, root):
        self.inorder_traverse(root)
        return self.valid

    def inorder_traverse(self, node):
        if not node:
            return

        self.inorder_traverse(node.left)
        if self.last_node and self.last_node.val >= node.val:
            self.valid = False
            return
        self.last_node = node
        self.inorder_traverse(node.right)

    def divide_conquer(self, node):
        if not node:
            return True, None, None

        l_valid, l_min, l_max = self.divide_conquer(node.left)
        r_valid, r_min, r_max = self.divide_conquer(node.right)

        # 左、右子树非二叉搜索树
        if not l_valid or not r_valid:
            return False, None, None

        # 左子树的最大值大于等于当前值
        if l_max and l_max.val >= node.val:
            return False, None, None

        # 右子树最小值小于等于当前值
        if r_min and r_min.val <= node.val:
            return False, None, None

        # 当前节点也是二叉搜索树
        c_min = l_min if l_min else node
        c_max = r_max if r_max else node

        return True, c_min, c_max

