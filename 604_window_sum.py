"""604 Windows Sum

Algorithm:
滑动窗口

Complexity:
O(k - 1) + O(n - k) = O(n - 1)
=O(n)
"""


class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        length = len(nums)
        if length < k or k <= 0:
            return []

        results = [0] * (length - k + 1)
        for i in range(k):
            results[0] += nums[i]

        for i in range(1, length - k + 1):
            results[i] = results[i - 1] + nums[i + k - 1] - nums[i - 1]

        return results

