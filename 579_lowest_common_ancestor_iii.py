"""579 Lowest Common Ancestor iii

Algorithm:
分治

Note:

"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def __init__(self):
        self.found = False
        self.result = None

    def lowestCommonAncestor3(self, root, A, B):
        self.lowestCommonAncestor_helper(root, A, B)
        return self.result

    def lowestCommonAncestor_helper(self, node, A, B):
        if node is None:
            return 0
        if self.found:
            return

        left = self.lowestCommonAncestor_helper(node.left, A, B)
        right = self.lowestCommonAncestor_helper(node.right, A, B)

        if left and right:
            self.found, self.result = True, node
            return

        if left or right:
            if node.val == A.val or node.val == B.val:
                self.found, self.result = True, node
                return
            return 1

        if node.val == A.val or node.val == B.val:
            return 1
        return 0


test_node = TreeNode(2)
test_node.left = TreeNode(1)
test_node.right = TreeNode(3)

sol = Solution()
print(sol.lowestCommonAncestor3(test_node, TreeNode(1), TreeNode(3)))

