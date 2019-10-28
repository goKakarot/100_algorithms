"""LintCode No.200 Longest Palindromic Substring

"""

class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longest_palindrome(self, s):
        if not s:
            return ''

        # search from the middle character to each side
        # each char has either odd and even possibility, but reuse the same find()
        # difference is the starting point
        longest_sub = ''
        for middle in range(len(s)):
            sub = self.find_palindrome_from(s, middle, middle)
            if len(sub) > len(longest_sub):
                longest_sub = sub
            sub = self.find_palindrome_from(s, middle, middle + 1)
            if len(sub) > len(longest_sub):
                longest_sub = sub
        return longest_sub

    def find_palindrome_from(self, s, left, right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longest_palindrome_M(self, s):
        s_M = ''
        # normally, operations to a string does not change the string value,
        # have to assign returned value to another variable
        for c in s:
            s_M = s_M.__add__('#')
            s_M = s_M.__add__(c)
        s_M = s_M.__add__('#')

        longest_sub = ''
        for middle in range(len(s_M)):
            sub = self.find_palindrome_from(s_M, middle, middle)
            if len(sub) > len(longest_sub):
                longest_sub = sub

        longest_sub = longest_sub.replace('#', '')
        return longest_sub


# write some test cases
sol = Solution()
test_odd_string = 'wabcdcbavcsc'
# even string has length of 8
test_even_string = 'wabcddcbav'
# print(sol.odd_longest_palindrome(4, test_odd_string))
# print(sol.even_longest_palindrome(4, test_even_string))

test_string = 'bb'
# ∂print(sol.longest_palindrome(test_string))
print(sol.longest_palindrome_M(test_string))

