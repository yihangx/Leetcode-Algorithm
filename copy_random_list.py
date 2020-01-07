class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def __init__(self):
        self.visit = {}

    def copy_random_list(self, head):
        if head == None:
            return None
        if head in self.visit:
            return self.visit[head]
        node = Node(head.val, None, None)
        self.visit[head] = node
        node.next = self.copy_random_list(head.next)
        node.random = self.copy_random_list(head.random)
        return node
