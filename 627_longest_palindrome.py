"""LintCode No.627 Longest Palindrome

"""


class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longest_palindrome(self, s):
        pairs, sum_p = [], 0
        for c in s:
            if c in pairs:
                sum_p = sum_p + 2
                pairs.remove(c)
            else:
                pairs.append(c)
        if pairs:
            sum_p += 1
        return sum_p

    def longest_palindrome_9(self, s):
        hash_p = {}
        for c in s:
            if c not in hash_p:
                hash_p[c] = True
            else:
                del hash_p[c]
        remove = len(hash_p)
        if hash_p:
            remove -= 1

        return len(s) - remove


# write some test cases
sol = Solution()
test_string = 'abccccdd'
print(sol.longest_palindrome_9(test_string))

