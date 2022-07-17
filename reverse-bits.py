class Solution:
    def reverseBits(self, n):
        retval = 0
        for i in range(32):
            bit = n >> i & 1
            retval = retval | bit << (32-1-i)
            
        return retval