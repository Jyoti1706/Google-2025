from typing import List


def isEmpty(stack):
    return len(stack) == 0


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = [-1 for _ in range(len(nums2))]
        stack = []
        for idx in range(len(nums2) - 1, -1, -1):
            while stack:
                if stack[-1] > nums2[idx]:
                    nge[idx] = stack[-1]
                    stack.append(nums2[idx])
                    break
                else:
                    stack.pop()
            if not stack:
                nge[idx] = -1
                stack.append(nums2[idx])
        result = []
        for num in nums1:
            for idx, number in enumerate(nums2):
                if num == number:
                    result.append(nge[idx])

        return result


class Solution2:
    """
    Constraint : No Duplicate element
    we can store nge hashmap and use stack for traversingLeetcode-496-next-greater-element-i.py
    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}
        output = []

        for i in reversed(nums2):
            while stack:
                # found nearest greater element
                if stack[-1] > i:
                    hashmap[i] = stack[-1]
                    stack.append(i)
                    break
                else:
                    stack.pop()

            # stack is empty initially or was popped till empty
            if not stack:
                hashmap[i] = -1
                stack.append(i)

        for j in nums1:
            output.append(hashmap[j])
        return output


if __name__ == '__main__':
    obj = Solution()
    nums2 = [5, 7, 1, 2, 6, 0]
    nums1 = [1, 5, 0]
    res = obj.nextGreaterElement(nums1, nums2)
    print("The next greater elements are")
    print(*res)
