class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == "":
            return 0
        sign = ""
        if s[0] == "-":
            sign = "-"
            s = s[1:]
        if s[0] == "+":
            sign = ""
            s = s[1:]
        numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        ans = ""
        for char in s:
            if char in numbers:
                ans += char
            else:
                break
        try:
            ans = int(ans)
            if sign == "-":
                ans = ans * -1
            if ans > 2147483647:
                return 2147483647
            elif ans < -2147483648:
                return -2147483648
            else:
                return ans
        except ValueError:
            return 0


obj = Solution()
s = " -042"
print(obj.myAtoi(s))
s = "1337c0d3"
print(obj.myAtoi(s))
s = "0-1"
print(obj.myAtoi(s))
