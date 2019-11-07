"""902 kth Smallest Element in a BST

Algorithm:
1. inorder traversal recursive
简单的inorder遍历bst。用一个self.l记录已经见过来多少个节点，用self.res来记录第k个节点。
不用使用stack去记录所有见过的k个节点。
2. iterative
先inorder非递归，再拆解while loop，优化空间
注意：将原来的while loop替换为k次的for loop，找k次就返回，
同时不需要再定义result变量储存结果，因为执行k的stack最后一位即为第k小的数

Complexity:
使用 Binary Search Tree Iterator 的方式（可以参考 binary search tree iterator 那个题）
用 stack，从第一个点开始，走 k-1 步，就是第 k 个点了。
时间复杂度是 O(h + k)O(h+k) h 是树的高度。
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        for i in range(k):
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

        return stack[-1].val
