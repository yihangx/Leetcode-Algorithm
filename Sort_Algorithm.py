nums = [3,6,1,2,9,0,4,5,5,12,18,9]

def bubble(nums):
    # O(n^2)
    m = len(nums)
    for i in range(m):
        print(nums)
        for j in range(1, m - i):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
    return nums

def selection(nums):
    # O(n^2)
    m = len(nums)
    for i in range(m):
        min = i
        for j in range(i+1, m):
            if nums[j] < nums[min]:
                min = j
        nums[min], nums[i] = nums[i], nums[min]
    return nums

def insertion(nums):
    # O(n^2)
    for index, value in enumerate(nums):
        while index > 0 and nums[index-1] > value:
            nums[index] = nums[index-1]
            index -= 1
        nums[index] = value
    return nums

def merge(nums):
    # IMPORTANT! O(nlogn)
    if len(nums) <= 1:
        return nums
    middle = len(nums) // 2
    left = merge(nums[:middle])
    right = merge(nums[middle:])
    return merge_sort(left, right)

def merge_sort(left, right):
    l = 0
    r = 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

def quick(nums):
    # IMPORTANT! O(nlogn) Worst:O(n^2)
    return qsort(nums, 0, len(nums)-1)
def qsort(nums, left, right):
    if left >= right:
        return
    m = left
    for i in range(left + 1, right + 1):
        if nums[i] < nums[left]:
            m += 1
            nums[m], nums[i] = nums[i], nums[m]
    nums[m], nums[left] = nums[left], nums[m]
    quick(nums, left, m - 1)
    quick(nums, m + 1, right)

print(merge(nums))
