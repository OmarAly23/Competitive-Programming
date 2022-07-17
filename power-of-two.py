import math
class Solution:
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        if n == 0:
            return None
        if n < 0:
            return False
        val = math.log2(n)
        if val.is_integer():
            return True
        return False

S = Solution()
print(S.isPowerOfTwo(3))