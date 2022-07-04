class Solution:

    def containsDuplicate(self, nums):
        list.sort(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True

        return False





S = Solution()
print(S.containsDuplicate([1,2,3,1]))
print(S.containsDuplicate([1,2,3,4]))
print(S.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
