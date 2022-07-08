class Solution:
    def sortedSquares(self, nums):
        squares = []
        for i in nums:
            squares.append(i*i)

        return sorted(squares)

S = Solution()
print(S.sortedSquares([-4, -1, 0, 3, 10]))
