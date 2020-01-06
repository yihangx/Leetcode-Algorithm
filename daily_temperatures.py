nums = [73, 74, 75, 71, 69, 72, 76, 73]

def daily_temp(nums):
    stack = []
    res = [0] * len(nums)
    for index, value in enumerate(nums):
        while stack and nums[stack[-1]] <= value:
            res[stack[-1]] = index - stack[-1]
            stack.pop()
        stack.append(index)
    return res

print(daily_temp(nums))
