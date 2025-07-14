class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        def power(x: int, num: int) -> int:
            if num == 0:
                return 1
            elif num & 1 == 0:
                return power(x ** 2 % MOD, num // 2)
            return x * power(x, num - 1) % MOD

        return 5 ** (n % 2) * power(20, n // 2) % MOD


obj = Solution()
print(obj.countGoodNumbers(4))
print(obj.countGoodNumbers(50))
