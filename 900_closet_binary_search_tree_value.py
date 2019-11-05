"""900 Closet Binary Search Tree Value

Algorithm:
递归和迭代都可以解决

Note:
1. 遍历
可以直接先用inorder得到整个排序的结果。然后在排序中找离target最近的那个值，
但是注意如果使用复杂度为O(n)，因为要再遍历数组一遍
2. 迭代
因为已经是bst，所以不需要先取得整个排序结果，而是直接在bst上利用bst的性质traverse最接近的数
每次查找计算node和target的绝对值，打擂台，最后输出结果
迭代对于复杂的二叉搜索树查找问题就不一定好想，只是这道题比较容易
3. 递归
bst搜索值问题用递归一定可以做出来，在bst上查找的过程其实是一个不断逼近target的过程。
利用binary search的思想，我们只需要high和low两个变量，
慢慢逼近target的上下限，最后判断high, low哪个更接近target
这道题递归书写比迭代复杂，这里又写一遍递归地意义在于，是否会出现题目的变形：找到值得上下界？

Complexity:
时间复杂度为O(h)
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

