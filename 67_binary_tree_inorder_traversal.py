"""67. Binary Tree Inorder Traversal
二叉树的中序遍历

二叉树测试用例选用最简单的，不要想下面子树的情况怎么办，都是可以循环解决的

只要有左子树就向下，保证左边永远是访问过的，这时只要处理是否有右子树：
# 有右子树
遍历右子树的所有左子树
# 无右子树
弹出栈

Note:
1. stack中只剩下root节点时的情况，stack[-1]数组越界

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
        if root is None or not root:
            return
        self.traversal(root.left)
        self.results.append(root.val)
        self.traversal(root.right)

    def traversal_non_recursive(self, root):
        if root is None or not root:
            return []

        stack = []
        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack[-1]
            self.results.append(node.val)
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            else:
                node = stack.pop()
                # Note.1
                while stack and stack[-1].right == node:
                    node = stack.pop()

        return self.results


# write some test cases
root_node = TreeNode(1)
left_node = TreeNode(2)
right_node = TreeNode(3)

root_node.left, root_node.right = left_node, right_node

sol = Solution()
print(sol.inorderTraversal(root_node))

