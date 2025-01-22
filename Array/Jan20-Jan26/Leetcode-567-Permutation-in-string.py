from collections import Counter
class Solution:
    # Todo: Retry
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        s1_len = len(s1)
        i = 0
        c2 = {}
        # check if S1 is Bigger than S2, Return FLase
        if s1_len > len(s2):
            return False
        # Initalize Dictionary of S1 length
        while s1_len - i > 0:
            c2[s2[i]] = c2.get(s2[i], 0) + 1
            i += 1
        # Check if initial dictionary have permutations
        if c2 == c1:
            return True
        # iterate through rest of String and Remove i-s1_len and add next data in dictionary.
        while i < len(s2):
            if c2 == c1:
                return True
            c2[s2[i-s1_len]] -= 1
            if c2[s2[i-s1_len]] == 0:
                del c2[s2[i-s1_len]]
            c2[s2[i]] = c2.get(s2[i], 0) + 1
            if c2 == c1:
                return True
            i += 1
        return False

obj = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(obj.checkInclusion(s1,s2))
s1 = "ab"
s2 = "eidboaoo"
print(obj.checkInclusion(s1,s2))


