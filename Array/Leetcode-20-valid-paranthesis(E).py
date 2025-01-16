class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"}": "{", "]": "[", ")": "("}

        stack = []
        for bracket in s:
            if bracket not in dic.keys():
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if last != dic[bracket]:
                    return False
        return len(stack) == 0


obj = Solution()
s="()"
print(obj.isValid(s))
s="[}"
print(obj.isValid(s))
