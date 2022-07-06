class Solution:

    def searchInsert(self, nums, target):
        if target < nums[0]:
            return 0

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
        
        tmp = nums
        index = binSearch(nums, target, 0, len(nums)-1)
        if index != -1:
            return index

        def searchIns(nums, target):

            if len(nums) == 1:
                if nums[0] == target:
                    return 0
                else:
                    index = binSearch(tmp, nums[0], 0, len(tmp)-1)
                    if nums[0] > target:
                        return index-1
                    else:
                        return index+1

            midpoint = len(nums)//2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                return searchIns(nums[0:midpoint], target)
            else:
                return searchIns(nums[midpoint:len(nums)], target)
        
        return searchIns(nums, target)        


S = Solution()
print(S.searchInsert([1,3,5], 5))
