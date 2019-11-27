def task_scheduler(tasks, n):
    c = list(map(tasks.count, set(tasks)))
    return max(sum(c), (max(c) - 1) * (n + 1) + c.count(max(c)))
