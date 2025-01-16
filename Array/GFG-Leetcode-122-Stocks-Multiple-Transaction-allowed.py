class Solution:
    def maxProfit(self, prices):
        lmin = prices[0]
        lmax = prices[0]
        n = len(prices)
        res = 0
        i = 0
        while i < n - 1:
            while i < n - 1 and prices[i] > prices[i + 1]:
                i += 1
            lmin = prices[i]

            while i < n - 1 and prices[i] < prices[i + 1]:
                i += 1
            lmax = prices[i]
            res += lmax - lmin
        return res

    def maximumProfit(self, prices) -> int:
        # code here
        res = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                res += prices[i + 1] - prices[i]
        return res
