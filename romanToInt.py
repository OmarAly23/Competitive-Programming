class Solution:
    def split_string(self, word):
        return [char for char in word]

    def romanToInt(self, s):
        dict = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000,
                'IV': 4,
                'IX': 9,
                'CD': 400,
                'CM': 900,
                'XL': 40,
                'XC': 90,
        }
        list_of_chars = self.split_string(s)
        sum = 0
        i = 1
        flag = 0
        skip = False
        length = len(list_of_chars)
        for l in list_of_chars:

            if flag == 1 and skip == True:
                flag = 0
                skip = False
                i += 1
                continue

            if i != length:

                if l == 'I' and list_of_chars[i] == 'V':
                    sum += dict['IV']
                    flag = 1
                    skip = True
                elif l == 'I' and list_of_chars[i] == 'X':
                    sum += dict['IX']
                    flag = 1
                    skip = True
                if l == 'C' and list_of_chars[i] == 'D':

                    skip = True
                    sum += dict['CD']
                    flag = 1
                    skip = True
                elif l == 'C' and list_of_chars[i] == 'M':
                    sum += dict['CM']
                    flag = 1
                    skip = True
                if l == 'X' and list_of_chars[i] == 'L':
                    sum += dict['XL']
                    flag = 1
                    skip = True
                elif l == 'X' and list_of_chars[i] == 'C':
                    sum += dict['XC']
                    flag = 1
                    skip = True

            if flag == 0 or (i == length):
                sum += dict[l]
            i += 1


        return sum

S1 = Solution()
print(S1.romanToInt('III'))
print(S1.romanToInt('LVIII'))
print(S1.romanToInt('MCMXCIV'))
#string = str(input('Enter string: '))
print(S1.romanToInt('MCMXCVI'))
print(S1.romanToInt("MMMXLV"))
print(S1.romanToInt("MCMXLVI"))
