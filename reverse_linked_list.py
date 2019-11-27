class listnode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution:
    def reversed_linked_list(self, head):
        prev = None
        while head:
            temp = head.next
            head.netx = prev
            prev = head
            head = temp
        return prev
