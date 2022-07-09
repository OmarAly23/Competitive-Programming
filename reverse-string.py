class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        def rev(s, pointer1, pointer2):
            if pointer1 >= pointer2:
                return s

            tmp = s[pointer1]
            s[pointer1] = s[pointer2]
            s[pointer2] = tmp
            return rev(s, pointer1+1, pointer2-1)

        return rev(s, 0, len(s)-1)


S = Solution()
print(S.reverseString(["h","e","l","l","o"]))
print(S.reverseString(["H","a","n","n","a","h"]))
