class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq=[0]*26
        for c in s:
            freq[ord(c)-ord('a')]+=1
        for i,c in enumerate(s):
            if freq[ord(c)-ord('a')]==1:
                return i
        return -1

    def firstUniqCharHashMap(self, s: str) -> int:
        mp = {}

        for a in s:
            mp[a] = mp.get(a, 0) + 1

        for i in range(len(s)):
            if mp[s[i]] == 1:
               return i

        return -1