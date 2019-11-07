"""67. Binary Tree Inorder Traversal

Algorithm:
1. 递归
2. 迭代（需要掌握）
iterative version可以看成是一个模版。即：
从root开始，一直路向左，把遇到的left children全部压入stk。（left）
每次从stk弹出一个左节点（current），然后指向其右节点，继续一路向左。(right)
一直到stk为空

Note:
traversal_non_recursive_simple()
引入dummy_node只需一个while loop

Complexity:
O(n)
"""


# Definition of TreeNode
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        self.results = []
        self.traversal_non_recursive(root)
        return self.results

    def traversal(self, root):
        if root is None:
            return
        self.traversal(root.left)
        self.results.append(root.val)
        self.traversal(root.right)

    def traversal_non_recursive(self, root):
        result = []
        stack = []

        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

        return result

    def traversal_non_recursive_simple(self, root):
        result = []
        stack = []

        dummy_node = TreeNode(0)
        dummy_node.right = root
        stack.append(dummy_node)

        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

            if stack:
                result.append(stack[-1].val)

        return result
