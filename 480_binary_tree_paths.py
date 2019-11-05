"""480 Binary Tree Paths

Algorithm:
分治：
自下而上的逻辑，返回条件为触碰到底边的叶子节点
遍历
自上而下的逻辑

Complexity:
O(n)
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # 处理输入为空集的情况
        if root is None:
            return []

        # 与其他分治不同的是，递归截止返回最后一个叶子节点
        if root.left is None and root.right is None:
            return [str(root.val)]

        left_paths = self.binaryTreePaths(root.left)
        right_paths = self.binaryTreePaths(root.right)

        paths = []
        for path in left_paths + right_paths:
            paths.append(str(root.val) + '->' + path)

        return paths

    def binaryTreePaths_dfs(self, root):
        if root is None:
            return []
        paths = []
        self.dfs(root, [str(root.val)], paths)
        return paths

    def dfs(self, node, path, paths):
        if node.left is None and node.right is None:
            # 需要记住join的使用方法，有返回值
            paths.append('->'.join(path))
            return

        if node.left:
            path.append(str(node.left.val))
            self.dfs(node.left, path, paths)
            path.pop()
        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, path, paths)
            path.pop()

