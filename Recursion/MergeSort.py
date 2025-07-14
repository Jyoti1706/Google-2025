def mergeArray(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    return result


def MergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])
    return mergeArray(left, right)


nums = [1, 6, 2, 7, 9, 0, 3, 4]
print(MergeSort(nums))
