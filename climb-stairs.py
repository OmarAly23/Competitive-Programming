import math
class Solution:
    def climbStairs(self, n: int) -> int:
        # Using Binet's Fibonacci formula:
        ans = ( pow((1+ math.sqrt(5))/2 , n+1) - pow((1-math.sqrt(5))/2, n+1) ) / math.sqrt(5)
        return round(ans)