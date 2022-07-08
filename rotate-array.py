class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """


        def checkIfDuplicates(listOfElems):
            if len(listOfElems) == len(set(listOfElems)):
                return False
            else:
                return True

        dict = {}

        if len(nums) == 1:
            return nums


        while k > len(nums):
            print('Here')
            if k % len(nums) == 0:
                return nums
            else:
                k = (k-len(nums))

        if len(nums) == 3:
            mindex = len(nums)
            for i in range(len(nums)):
                if (i + k) >= mindex:
                    inc = (i+k) - mindex
                    if inc % len(nums) == 0:
                        inc = 0
                else:
                    inc = i+k
                dict[nums[i]] = inc

            for i in dict:
                nums[dict[i]] = i

            return nums

        if checkIfDuplicates(nums):
            mindex = len(nums)
            l = []
            l1 = []
            for i in range(len(nums)):
                if (i + k) >= mindex:
                    inc = (i + k) - mindex
                    dict[nums[i]] = inc
                    l.append(nums[i])
                    l1.append(inc)
                else:
                    dict[nums[i]] = i+k
                    l.append(nums[i])
                    l1.append(i+k)

            retval = zip(l,l1)
            ite = 0
            for i in retval:
                # i[0] contains the key itself
                # i[1] contains the index
                nums[i[1]] = i[0]
                ite += 1
            return nums


        mindex = len(nums)
        for i in range(len(nums)):
            if (i + k) >= mindex:
                inc = (i + k) - mindex
                dict[nums[i]] = inc
            else:
                dict[nums[i]] = i+k

        for i in dict:
            nums[dict[i]] = i
        return nums
