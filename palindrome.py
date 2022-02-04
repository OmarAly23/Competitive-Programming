class Solution:
    def palindrome(self, x):
        strint = str(x)
        rev = strint[::-1]
        if rev == strint:
            return True
        return False

num = -121
S1 = Solution()
pa = S1.palindrome(num)
print(pa)
