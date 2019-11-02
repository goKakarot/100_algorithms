"""66. Binary Tree Preorder Traversal
二叉树的前序遍历
# 递归
递归地找左子树，找完再递归地找右子书
# 非递归
非递归实现前序遍历时，首先存入当前节点的值，然后将右子树压入栈中，再将左子树压入栈中。
对栈中元素遍历，不断重复改过程

Definition of TreeNode:
class tree_node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        self.results = []
        self.traverse_recursive(root)
        return self.results

    def traverse_recursive(self, root):
        if root is None or not root:
            return
        self.results.append(root.val)
        self.traverse_recursive(root.left)
        self.traverse_recursive(root.right)

    def traverse_non_recursive(self, root):
        if root is None or not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            self.results.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

