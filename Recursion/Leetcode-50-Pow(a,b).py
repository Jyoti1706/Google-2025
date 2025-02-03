class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x  # Handle negative powers by inverting x
            n = -n
        return self.Power(x, n)

    def Power(self, x, n):
        if n == 0:
            return 1
        half = self.Power(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

obj = Solution()
print(obj.myPow(2.0, -2))
print(obj.myPow(2.0, 10))
