"""95 Validate Binary Search Tree

Algorithm:
1. 二叉搜索树的inorder遍历结果升序
2. 分治法
注意是left subtree上的所有节点都小于root；right subtree上的所有节点都大于root。
所以我们遍历左／右子数，找到subtree分别的最大最小值 然后跟root进行判断
3. 迭代
中序遍历的迭代，唯一不同的是最后进行比较判断是否为有效BST
Note:
1. 注意，需要判断l_max, l_min, r_max, r_min是否为空，
最后一个节点的情况
2. node可能在不断左移中被置None，所以不可信，不能用来进行比较。
第一次要提前赋值，还有if判断内要更新pre_node
Complexity:
O(n)
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
        # see Note.1
        if l_max and l_max.val >= node.val:
            return False, None, None

        # 右子树最小值小于等于当前值
        if r_min and r_min.val <= node.val:
            return False, None, None

        # 当前节点也是二叉搜索树
        # see Note.1
        c_min = l_min if l_min else node
        c_max = r_max if r_max else node

        return True, c_min, c_max

    def isValidBST_iterative(self, root):
        if root is None:
            return True

        stack = []
        while root:
            stack.append(root)
            root = root.left

        # see Note.2
        pre_node = stack[-1]
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                if pre_node.val >= stack[-1].val:
                    return False
                # see Note.2
                pre_node = stack[-1]
        return True

