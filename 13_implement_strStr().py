"""LintCode No.13 Implement strStr()

"""


class Solution:
    """
    @param source:
    @param target:
    @return: if find return index, if not return -1
    """
    def str_string(self, source, target):
        self.is_not_used()
        len_s = len(source)
        len_t = len(target)
        # two corner cases
        # source = None or target = None
        # target = ''
        if source is None or target is None:
            return -1
        if len_t == 0:
            return 0

        for i in range(len_s - len_t + 1):
            # compare the first char, if match go further
            # otherwise skip. this improves speed
            if source[i] != target[0]:
                continue
            for j in range(len_t):
                if source[i + j] != target[j]:
                    break
                # this if has to put inside the for loop,
                # e.g., target[last] != source[i + last]
                if j == len_t - 1:
                    return i
        return -1

    def is_not_used(self):
        pass


# write some test cases
sol = Solution()
source = 'mississippi'
target = 'issip'
print(sol.str_string(source, target))

