from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        allowed = {"D", "C", "+"}
        output = []
        for operation in operations:
            if operation in allowed:
                if operation == "D":
                    ele = output[-1] * 2
                    output.append(ele)
                elif operation == "C":
                    output.pop()
                else:
                    op1 = output.pop()
                    op2 = output.pop()
                    op3 = op1 + op2
                    output.append(op2)
                    output.append(op1)
                    output.append(op3)
            else:
                output.append(int(operation))
        return sum(output)


# obj = Solution()
# ops = ["5", "2", "C", "D", "+"]
# print(obj.calPoints(ops))
obj = Solution()
ops = ["5","-2","4","C","D","9","+","+"]
print(obj.calPoints(ops))
