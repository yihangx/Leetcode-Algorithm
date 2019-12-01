tasks = ["A","A","A","B","B","B"]
n = 2

class Solution:
    def leastInterval(self, tasks):
        c = list(map(tasks.count, set(tasks)))
        return max(sum(c), (max(c) - 1) * (n + 1) + c.count(max(c)))