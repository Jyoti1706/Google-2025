from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def Solve(open, close, current):
            if open == 0 and close == 0:
                result.append(current)
                return
            if open == close:
                Solve(open-1, close, current+"(")
            elif open == 0:
                Solve(open, close-1, current+")")
            else:
                Solve(open-1, close, current+"(")
                Solve(open, close-1, current+")")
        Solve(n-1,n, "(")
        return result
obj = Solution()
print(obj.generateParenthesis(3))
print(obj.generateParenthesis(2))
print(obj.generateParenthesis(1))
