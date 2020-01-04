def remove_duplicates1(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

def remove_duplicates2(head):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    while head and head.next:
        if head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            head = head.next
            current.next = head
        else:
            current = current.next
            head = head.next
    return dummy.next
