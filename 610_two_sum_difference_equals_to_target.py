"""610 Two Sum Difference Equals to Target

Algorithm:
双指针

Notes:
1. 取绝对值是堤防target为负数时的情况，因为排序后我们的比较环境总是正数，
则永远比target大，找不到结果
e.g.,
[1,0,-1]
-2
2. enumerate/lambda
lambda: 省去为实际创建一个函数
enumerate: 枚举list中的每一个元素并加上索引
"""


class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # Note.1
        target = abs(target)
        nums = [(nums, i) for i, nums in enumerate(nums)]
        nums = sorted(nums, key=lambda x: x[0])

        n = len(nums)
        j, index = 0, []
        for i in range(n):
            if i == j:
                j += 1
            while j < n and nums[j][0] - nums[i][0] < target:
                j += 1
            if j < n and nums[j][0] - nums[i][0] == target:
                index = [nums[i][1] + 1, nums[j][1] + 1]

        if index[0] > index[1]:
            index[0], index[1] = index[1], index[0]

        return index

