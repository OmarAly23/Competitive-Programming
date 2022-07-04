class Solution:
    def search(self, nums, target):
        def binSearch(nums, target, low, high):

            if len(nums) == 1:
                if nums[0] == target:
                    return 0
                else:
                    return -1

            if low > high:
                return -1

            else:
                mid = (low+high)//2

                if target == nums[mid]:
                    return mid
                elif target >  nums[mid]:
                    low = mid + 1
                    return binSearch(nums, target, low, high)
                else:
                    high = mid - 1
                    return binSearch(nums, target, low, high)

        return binSearch(nums, target, 0, len(nums)-1)




S = Solution()
print(S.search([-1,0,5], -1))
