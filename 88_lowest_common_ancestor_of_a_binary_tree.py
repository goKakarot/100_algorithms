"""88 Lowest Common Ancestor of a Binary Tree

Algorithm:
分治（递归）

Note:
1. 这道题的一个重要前提是树中一定存在LCA，所以简单遍历所有节点，
截止返回条件为A或B等于自己时，返回当前节点值，类似前序遍历
2. 看到左有值右为空时，可能左边只有一个值，
也可能左边存在有效LCA（这种情况层层返回后还是会得到答案）
3. 四种情况

Complexity:
O(n)
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        node = self.lowestCommonAncestor_helper(root, A, B)
        return node

    def lowestCommonAncestor_helper(self, node, A, B):
        if node is None:
            return None

        if node == A or node == B:
            return node

        left = self.lowestCommonAncestor_helper(node.left, A, B)
        right = self.lowestCommonAncestor_helper(node.right, A, B)

        if left and right:
            return node
        # see Note.2
        if left:
            return left
        if right:
            return right
        return 0

