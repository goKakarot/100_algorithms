"""56 Two Sum

1. Hash
Hash方法使用一个Hashmap结构来记录对应的数字是否出现，以及其下标。时间复杂度为O(n)O(n)。
空间上需要开辟Hashmap来存储, 空间复杂度是O(n)O(n)。

2. Two Pointers
基于有序数组的特性，不断移动左右指针，减少不必要的遍历，时间复杂度为排序的O(nlogn)，
主要是排序的复杂度。但是在空间上，不需要额外空间，因此额外空间复杂度是 O(1)O(1)
"""


class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        hash_dict = dict()

        for i in range(len(numbers)):
            if (target - numbers[i]) in hash_dict:
                return hash_dict[target - numbers[i]], i
            hash_dict[numbers[i]] = i
        return None

    def twoSum_twoPointters(self, numbers, target):
        numbers.sort()

        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return numbers[left], numbers[right]
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return None

