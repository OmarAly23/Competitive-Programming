# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n):
        if isBadVersion(1):
            return 1
        l = 0
        r = n
        bad = n // 2
        while l <= r:
            midpoint = (l + r)//2
            if isBadVersion(midpoint):
                r = midpoint - 1
                bad = midpoint
            else:
                l = midpoint + 1
        return bad



