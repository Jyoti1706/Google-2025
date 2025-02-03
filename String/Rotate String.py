class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = s+s
        i = 0
        n = len(goal)
        find = False
        while i+n < len(s):
            if s[i:i+n] == goal:
                find = True
                break
            i += 1
        return True if find else False


obj = Solution()
s = "abcde"
goal = "cdeab"
print(obj.rotateString(s,goal))

s = "abcde"
goal = "fdeab"
print(obj.rotateString(s,goal))