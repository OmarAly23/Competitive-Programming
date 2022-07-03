class Solution:


    def unique(self, st):

        # String length cannot be more than
        # 256.
        if len(st) > 256:
            return False

        # Initialize occurrences of all characters
        char_set = [False] * 128

        # For every character, check if it exists
        # in char_set
        for i in range(0, len(st)):

            # Find ASCII value and check if it
            # exists in set.
            val = ord(st[i])
            if char_set[val]:
                return False

            char_set[val] = True

        return True

    def maxLength(self, L):
        Mlength = 0
        for ele in L:
            tmp = len(ele)
            if tmp >= Mlength:
                Mlength = tmp
        return Mlength

    def lengthOfLongestSubstring(self, s):
        if self.unique(s):
            return len(s)

        flag = 0
        index = 0
        # you want to store all substrings
        list_of_substrings = []

        for element in s:
            flag = 0
            innerList = []
            for i in range(index, len(s)):
                print(s[i])
                print(f'Outside Loop Index: {index} Element: {element} s: {s[i]}')
                print('---------------------------------------------------------')
                if element == s[i] and flag == 0:
                    print(f'First Index: {index} Element: {element} s: {s[i]}')
                    print('---------------------------------------------------------')
                    innerList.append(s[i])
                    flag = 1
                elif element == s[i] and flag == 1:
                    print(f'Second Index: {index} Element: {element} s: {s[i]}')
                    print('---------------------------------------------------------')
                    list_of_substrings.append(innerList)
                    break
                elif element != s[i] and (flag == 0 or flag == 1):
                    print(f'Third Index: {index} Element: {element} s: {s[i]}')
                    print('---------------------------------------------------------')
                    if s[i] in innerList:
                        print(f'S: {s[i]} Inner List: {innerList}')
                        list_of_substrings.append(innerList)
                        break
                    else:
                        print(f'S element: {s[i]}')
                        print('---------------------------------------------------------')
                        innerList.append(s[i])
                    print(f'Inner List: {innerList}')
                    print('---------------------------------------------------------')
                if element != s[i] and (flag == 1 and i == len(s)-1):
                    print(f'Fourth Index: {index} Element: {element} s: {s[i]}')
                    print('---------------------------------------------------------')
                    print(f'Inner List: {innerList}')
                    list_of_substrings.append(innerList)
                    break
            index += 1

        print(list_of_substrings)
        return self.maxLength(list_of_substrings)


S1 = Solution()
val2 = S1.lengthOfLongestSubstring('abcabcbb')
val1 = S1.lengthOfLongestSubstring('bbbbb')
val = S1.lengthOfLongestSubstring('pwwkew')

print(f'Case1: {val2}')
print(f'Case2: {val1}')
print(f'Case3: {val}')

s = str(input('Enter string: '))
print(S1.lengthOfLongestSubstring(s))
