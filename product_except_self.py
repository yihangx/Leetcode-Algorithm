nums = [1,2,3,4]

def product_except_self(nums):
    p = 1
    res = []
    for i in range(len(nums)):
        res.append(p)
        p = p * nums[i]
    p = 1
    for i in reversed(range(len(nums))):
        res[i] = res[i] * p
        p = p * nums[i]
    return res

print(product_except_self(nums))
