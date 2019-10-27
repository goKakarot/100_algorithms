"""LintCode No.415 Valid Palindrome

"""


class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    def is_palindrome(self, s):
        self.is_not_used()
        s = s.lower()
        left, right = 0, len(s) - 1

        # '' or ' ' makes left >= right(e.g. 0 > -1 or 0 = 0), and return True
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    # PyCharm "thinks" that you might have wanted to have a static method, but you forgot to declare it to be static.
    #
    # is_palindrome method does not use self in its body and hence does not actually change the class instance.
    # Hence the method could be static.
    def is_not_used(self):
        pass


# let's write some test cases
sol = Solution()
a_str = 'A man, a plan, a canal: Panama'

print(sol.is_palindrome(s=' '))

