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
