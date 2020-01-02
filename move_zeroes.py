nums = [0,1,0,3,12]

def move_zeroes(nums):
    res = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[res] = nums[res], nums[i]
            res += 1

print(move_zeroes(nums))
