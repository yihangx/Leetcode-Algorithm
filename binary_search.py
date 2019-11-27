nums = [1,3,4,5,6,7,8,9,12,42,122]
target = 12

def binary(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if nums[middle] == target:
            return middle
        if target < nums[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1

print(binary(nums, target))
