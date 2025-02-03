import math


class Solution:
    def minimizeResult(self, expression: str) -> str:
        left, right = expression.split("+")
        lft = [left[0:i] + "(" + left[i:] for i in range(len(left))]
        rgt = [right[0:i] + ")" + right[i:] for i in range(1, len(right) + 1)]
        result = [math.inf, -1]
        for l in lft:
            for r in rgt:
                exp = l + "+" + r
                exp = exp.replace(")", ")*").replace("(", "*(").strip("*")
                result = (eval(exp), exp.replace("*", "")) if result[0] > eval(exp) else result
        return result[1]


class Solution2:
    def minimizeResult(self, expression: str) -> str:  # Example:  "247+38"
        #   left, right = "247","38"
        left, right = expression.split('+')
        value = lambda s: eval(s.replace('(', '*(').replace(')', ')*').strip('*'))

        lft = [left[0:i] + '(' + left[i:] for i in range(len(left))]  # lft = ['(247', '2(47', '24(7']
        rgt = [right[0:i] + ')' + right[i:] for i in range(1, len(right) + 1)]  # rgt = ['3)8', '38)']

        return min([l + '+' + r for l in lft for r in rgt], key=value)  # = min[(247+3)8,(247+38),2(47+3)8,2(47+38),24(7+3)8,24(7+38)]
                                                                        #             |       |         |        |        |        |
                                                                        #           2000     285       800      170     1920     1080
                                                                        #                                        |
                                                                        #                                   return 2(47+38)

obj = Solution()
expression = "999+999"
print(obj.minimizeResult(expression))

expression = "247+38"
print(obj.minimizeResult(expression))

expression = "12+34"
print(obj.minimizeResult(expression))
