nums = [100, 4, 200, 1, 3, 2]

def longest_consecutive_sequence(nums):
    nums = set(nums)
    res = 0
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1
            res = max(res, y - x)
    return res

print(longest_consecutive_sequence(nums))
