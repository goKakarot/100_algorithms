"""453 Flatten Binary Tree to Linked List

Algorithm:
分治：（返回最后一个节点）
情况      操作  返回值
左有右有  swap  right_last
左有右无  swap  left_last
左无右有  N/A   right_last
左无右无  N/A   node

前序遍历求链表：（要求掌握）
在进行self.flatten(root.left)的时候 root.right会发生改变
（在flatten root.left中 last_node是现在的root，而在flatten root.left中 last_node.right会变化，即对应现在的root.right也会发生变化）
所以要留一个临时变量存储此时的root.right值，保证在进行self.flatten(root.right)时，此时的root.right 不收到上一行的子函数self.flatten(root.left)的干扰

Complexity:
O(n)
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        self.flatten_linked_list(root)

    def flatten_linked_list(self, node):
        if node is None:
            return None

        left_last = self.flatten_linked_list(node.left)
        right_last = self.flatten_linked_list(node.right)

        if left_last is not None:
            left_last.right = node.right
            node.right = node.left
            node.left = None

        return right_last or left_last or node


class SolutionTraversal:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    last_node = None

    def flatten(self, root):
        if root is None:
            return None

        if self.last_node is not None:
            self.last_node.right = root
            self.last_node.left = None

        self.last_node = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)

