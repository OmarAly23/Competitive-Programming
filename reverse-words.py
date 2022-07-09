class Solution:
    def reverseWords(self, s):

        def rev(str):
            return str[::-1]

        L = []
        tmp = s.split(' ')
        innerL = ''
        for i in range(len(tmp)):
            if i != len(tmp)-1:
                innerL += (rev(tmp[i])) + ' '
            else:
                innerL += (rev(tmp[i]))

        return innerL
        
S = Solution()
print(S.reverseWords("Let's take LeetCode contest"))
