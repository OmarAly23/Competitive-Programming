import math
class Solution:

    @staticmethod
    def reverse(num):

        def checkContraint(num):
            constraint = math.pow(2,31)
            negContraint = math.pow(2,-31) - 1

            if num < constraint and num > negContraint:
                return True
            return False

        turnToString = str(num)
        if '.' in turnToString:
            turnToString = turnToString.split('.')
            intStr = str(turnToString[0])
        else:
            intStr = str(turnToString)
            intStr = str(intStr)

        if intStr[0] == '-':
            intStr = intStr[1:]
            revString = intStr[::-1]
            rev = int(revString)
            if checkContraint(rev):
                return -rev
            else:
                return 0

        revString = intStr[::-1]
        if revString[0] == '0' and len(revString) > 1:
            revString = revString[1:]
            rev = int(revString)
            if checkContraint(rev):
                return rev
            else:
                return 0
        revString = intStr[::-1]
        rev = int(revString)
        if checkContraint(rev):
            return rev
        else:
            return 0




num = -123
S1 = Solution()
rev = S1.reverse(num)
print(rev)
