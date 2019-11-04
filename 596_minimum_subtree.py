"""596 Minimum Subtree

Algorithm:
两种解法，Divide Conquer + Traverse, Pure Divide Conquer
形式上看起来差不多，但是从思路上来看：
第一个还是以每个node为中心，遍历了所有node的sum，对结果和全局变量进行比较（打擂台）
第二个是分别算出左右的结果（即各自最小子树节点位置和值），再比较left_min, right_min and curr_sum

Note:
1. 假设的初始最小值应当设为float('inf')一个非常大的值
不能设为0，假如root = {1, 2}，则返回结果为0，错误

Complexity:
O(n)

"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def __init__(self):
        self.node = None
        self.value = float('inf')

    def findSubtree(self, root):
        self.find_min_subtree(root)
        return self.node

    def find_min_subtree(self, node):
        if node is None:
            return 0

        left_sum = self.find_min_subtree(node.left)
        right_sum = self.find_min_subtree(node.right)

        curr_sum = left_sum + right_sum + node.val
        if curr_sum < self.value:
            self.value = curr_sum
            self.node = node

        return curr_sum

    def find_min_subtree_pure_dc(self, node):
        if node is None:
            # left_node, left_min, left_sum
            return None, float('inf'), 0

        left_node, left_min, left_sum = self.find_min_subtree(node.left)
        right_node, right_min, right_sum = self.find_min_subtree(node.right)

        curr_sum = left_sum + right_sum + node.val
        if left_min == min(left_min, right_min, curr_sum):
            return left_node, left_min, curr_sum
        if right_min == min(left_min, right_min, curr_sum):
            return right_node, right_min, curr_sum
        return node, curr_sum, curr_sum

