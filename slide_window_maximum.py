nums = [1,3,-1,-3,5,3,6,7]
k = 3
import collections

def slide_window(nums, k):
    res = []
    deq = collections.deque()
    for index, value in enumerate(nums):
        while deq and nums[deq[-1]] <= value:
            deq.pop()
        deq += [index]
        if index - deq[0] == k:
            deq.popleft()
        if index + 1 >= k:
            res.append(nums[deq[0]])
    return res

print(slide_window(nums, k))
