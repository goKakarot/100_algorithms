"""900 Closet Binary Search Tree Value

Algorithm:
递归和迭代都可以解决

Note:
1. 迭代
书写简单，每次搜索记录节点和target的绝对值，绝对值打擂台，最后输出
迭代对于复杂的二叉搜索树查找问题就不一定好想，只是这道题比较容易
2. 递归
这道题递归书写比迭代复杂，二叉搜索树搜索值问题用递归一定可以做出来，实际解决起来逻辑很直接
这里又写一遍递归地意义在于，是否会出现题目的变形：找到值得上下界？

Complexity:
时间复杂度为O(h)，注意如果使用inorder traversal，时间复杂度为O(n)因为要再遍历数组一遍
复杂度不是O(logn)因为BST并不保证树高为logn，除非是平衡二叉搜索树
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        closet_value = root.val
        while root:
            if abs(root.val - target) < abs(closet_value - target):
                closet_value = root.val
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return closet_value

    def closetValue_recursive(self, root, target):
        lower = self.find_lower_bound(root, target)
        upper = self.find_upper_bound(root, target)

        # 考虑只有上界或只有下界的情况，直接返回
        if lower is None:
            return upper.val
        if upper is None:
            return lower.val

        if target - lower.val >= upper.val - target:
            return upper.val
        return lower.val

    def find_lower_bound(self, node, target):
        if node is None:
            return None

        # 假如lower还在左边，交由下层继续处理
        # 一定能返回一个结果
        if target < node.val:
            return self.find_lower_bound(node.left, target)

        # 假如自己比lower小，两种情况
        # 1. 自己就是lower
        # 2. lower还在下层的右边，交由下层处理
        lower = self.find_lower_bound(node.right, target)
        return node if lower is None else lower

    def find_upper_bound(self, node, target):
        if node is None:
            return None

        if target >= node.val:
            return self.find_upper_bound(node.right, target)

        upper = self.find_upper_bound(node.left, target)
        return node if upper is None else upper

