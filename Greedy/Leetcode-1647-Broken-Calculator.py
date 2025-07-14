class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        operations = 0
        while startValue != target:
            if target < startValue:
                return operations + (startValue-target)
            elif target%2 == 0:
                operations += 1
                target = target//2
            else:
                operations += 1
                target += 1
        return operations
