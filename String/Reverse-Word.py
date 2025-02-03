class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        ans = []
        for idx , st in enumerate(s):
            if s[idx].strip() != "":
                ans.append(s[idx].strip())
        ans = ans[::-1]
        return " ".join(ans)

s = "a good   example"
obj = Solution()
print(obj.reverseWords(s))