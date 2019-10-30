# 在数据结构中，哈希函数是用来将一个字符串（或其他类型）转化为小于哈希表大小且大于等于零的整数。
# 一个好的哈希函数应该尽量避免冲突
# 一种广泛使用的哈希函数是使用数值33，以33为幂次底构造哈希值，使任何字符都是基于33的一个大整数
#
# 哈希函数的实现
# 1. 如何快速计算获取哈希值
#    霍纳法则，an * x^n + a(n-1) * x^(n-1) + ... a1 * x + a0 * 1
#             提取x项进行多项式转换
# 2. 如何让元素在哈希表中均匀分布
#    选择质数为常量
#
# Ref: https://blog.csdn.net/weixin_42339197/article/details/99544523


class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode(self, key, HASH_SIZE):
        ans = 0
        for c in key:
            ans = ans * 33 + ord(c)

        hash_value = ans % HASH_SIZE
        return hash_value


# write some test cases
sol = Solution()
test_string = 'abcd'
print(sol.hashCode(test_string, 1000))

