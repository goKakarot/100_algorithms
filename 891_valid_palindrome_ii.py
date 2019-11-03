"""891 Valid Palindrom II

"""


class Solution:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        length = len(s)
        left, right = self.two_pointers(s, 0, length - 1)
        if left >= right:
            return True
        return self.is_valid(s, left + 1, right) or self.is_valid(s, left, right - 1)

    def is_valid(self, s, left, right):
        left, right = self.two_pointers(s, left, right)
        return left >= right

    def two_pointers(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1
        return left, right

