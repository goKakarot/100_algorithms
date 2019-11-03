"""521 Remove Duplicate Numbers in Array

1. hash
把所有的数扔到 hash 表里，然后就能找到不同的整数有哪些。但是这种做法会耗费额外空间 O(n)O(n)
# O(n) time, O(n) space

2. two pointers（十分巧妙，需要掌握）
首先将数组排序，这样那些重复的整数就会被挤在一起。然后用两根指针，一根指针走得快一些遍历整个数组，
另外一根指针，一直指向当前不重复部分的最后一个数。
快指针发现一个和慢指针指向的数不同的数之后，就可以把这个数丢到慢指针的后面一个位置，并把慢指针++。
# O(nlogn) time, O(1) extra space
"""


class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        hash_dict = {}
        length = 0
        for num in nums:
            if num not in hash_dict:
                hash_dict[num] = True
                nums[length] = num
                length += 1
        return length

    # Brilliant tricks!
    def deduplication_2pointers(self, nums):
        length = len(nums)
        if not length:
            return 0

        nums.sort()
        result = 1
        for i in range(1, length):
            if nums[i] != nums[i - 1]:
                nums[result] = nums[i]
                result += 1
        return result

