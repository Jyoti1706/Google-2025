class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0 for h in height]
        postfix = [0 for h in height]
        val = 0
        ## populate prefix array
        for i in range(1, len(height)):
            prefix[i] = max(height[i - 1], prefix[i - 1])

        for j in range(len(height) - 2, -1, -1):
            postfix[j] = max(height[j + 1], postfix[j + 1])

        water = []
        for i in range(len(height)):
            curr = min(prefix[i], postfix[i]) - height[i]
            if curr < 0:
                water.append(0)
            else:
                water.append(curr)
        return sum(water)

