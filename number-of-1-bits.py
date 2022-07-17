class Solution:
    def hammingWeight(self, n):
        n = str(bin(n))
        counter = 0
        for i in n:
            if i == "1":
                counter +=1
        return counter

