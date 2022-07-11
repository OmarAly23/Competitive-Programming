
class Solution:
    def checkInclusion(self, s1, s2):
        counter, s1len = Counter(s1), len(s1)

        for i in range(len(s2)):
            if s2[i] in counter:
                counter[s2[i]] -= 1
            if i >= s1len and s2[i-s1len] in counter:
                counter[s2[i-s1len]] += 1

            if all([counter[i] == 0 for i in counter]):
                return True

        return False


S = Solution()
print(S.checkInclusion("ab", "eidboaoo"))
