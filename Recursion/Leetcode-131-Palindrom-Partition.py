def isPalindrome(word):
    return word == word[::-1]
class Solution:
    def partition(self, s: str):
        result = []
        n = len(s)

        def backtracking(s, idx, current):
            if idx >= n:
                result.append(current.copy())
                return
            for i in range(idx, n):
                if isPalindrome(s[idx:i+1]):
                    current.append(s[idx:i+1])
                    backtracking(s, i + 1, current)   # <= 2^n(posibility) * n(palindrome)
                    current.pop()

        backtracking(s,0, [])
        return result

obj = Solution()
s = "aab"
print(obj.partition(s))
s = "aaa"
print(obj.partition(s))