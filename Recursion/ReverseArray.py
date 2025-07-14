def ReverseUsing2Pointer(nums, l, r):
    if l > r:
        return
    nums[l], nums[r] = nums[r], nums[l]
    ReverseUsing2Pointer(nums, l+1, r-1)

def palindrome(data, i, n ):
    if i >= n//2:
        return True
    if data[i] != data[n-1-i]:
        return False
    return palindrome(data, i+1, n)



nums = [1,2,3,4,5]
ReverseUsing2Pointer(nums,0, len(nums)-1)
print(nums)
nums = [1,1,2,1,1]
print(palindrome(nums,0, len(nums)))
nums = [3,1,1,1,1,3]
print(palindrome(nums,0, len(nums)))