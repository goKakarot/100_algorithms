"""68. Binary Tree Postorder Traversal

Algorithm:
对于二叉树的遍历，在初期思考时往往只要考虑三种情况对应三个分支
根节点向下搜索，左子树向上，右子树向上
以这三种情况为思考依据，建立算法的基本骨架

Complexity:
二叉树的遍历时间复杂度是O(N)，N代表二叉树的节点个数，因为遍历所有节点
递归的时间复杂度为O(m * n)，m为递归的层数，n表示每层递归地运算次数
二叉树的递归，层数为n，每层遍历2^(n-1)个节点：
2^0 + 2^1 + 2^2 + ... + 2^(n-1) ~ 2^(n-1)?
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
    def post_order_traversal(self, root):
        self.results = []
        result = self.traversal_non_recursive(root)
        return result

    def traversal(self, root):
        if root is None and not root:
            return []

        self.traversal(root.left)
        self.traversal(root.right)
        self.results.append(root.val)


    def traversal_non_recursive(self, root):
        if not root:
            return []

        stack, result = [], []
        prev, curr = None, root

        stack.append(root)
        while stack:
            curr = stack[-1]
            # traverse down
            if not prev or prev.left == curr or prev.right == curr:
                if curr.left:
                    stack.append(curr.left)
                elif curr.right:
                    stack.append(curr.right)
                # no need, when we reach the end of the left node
                # left this case slip to the 'else' branch
                # else:
                #     result.append(curr.val)
                #     stack.pop()

            # traverse up from the left
            elif curr.left == prev:
                if curr.right:
                    stack.append(curr.right)
            # traverse up from the right
            else:
                result.append(curr.val)
                stack.pop()

            prev = curr

        return result


# write some test cases
test_node = TreeNode(1)
test_node_l = TreeNode(2)
test_node_r = TreeNode(3)
test_node.left, test_node.right = test_node_l, test_node_r

sol = Solution()
print(sol.traversal_non_recursive(test_node))