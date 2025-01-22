class Solution:

    def majorityElement(self, nums):
        n = len(nums)//3
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        output = []
        for key in counter:
            if counter[key] >= n:
                output.append(key)
        return output