nums = [7,7,5,7,5,1,5,7,5,5,7,7,7,7,7]

def majority_vote(nums):
    count = 0
    res = 0
    for n in nums:
        if n == res:
            count += 1
        elif count == 0:
            res, count = n, 1
        else:
            count -= 1
    return res

print(majority_vote(nums))
