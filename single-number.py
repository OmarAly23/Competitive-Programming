from this import d


class Solution:
    def singleNumber(self, nums):
        if len(nums) == 1:
            return nums[0]
  
        dict = {}
        
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        for i, key in dict.items():
            if key == 1:
                return i



S = Solution()
retval = S.singleNumber([2,2,1])
print(retval)
print(S.singleNumber([4,1,2,1,2]))