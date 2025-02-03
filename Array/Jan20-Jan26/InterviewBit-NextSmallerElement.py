class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        n = len(A)
        nse = [-1] * n
        stack = []
        for idx, num in enumerate(A):
            while stack:
                if stack[-1] < num:
                    nse[idx] = stack[-1]
                    stack.append(num)
                    break
                else:
                    stack.pop()
            if not stack:
                stack.append(num)
        return nse

A = [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
obj = Solution()
print(obj.prevSmaller(A))
