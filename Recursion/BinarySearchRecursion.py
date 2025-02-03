def BinarySearchRecursion(nums, target, left, right):
    if left > right:
        return len(nums) + 1
    mid = (left + right) // 2

    if nums[mid] == target:
        leftRecursion = BinarySearchRecursion(nums, target, left, mid - 1)
        return min(mid, leftRecursion)
    elif nums[mid] > target:
        leftRecursion = BinarySearchRecursion(nums, target, left, mid - 1)
        return leftRecursion
    else:
        rightRecursion = BinarySearchRecursion(nums, target, mid + 1, right)
        return rightRecursion


nums = [1, 2, 3, 4, 5]
print(BinarySearchRecursion(nums, 4, 0, len(nums)))
