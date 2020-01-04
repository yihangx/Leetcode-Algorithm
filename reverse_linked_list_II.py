def reversed_linked_list_II(head, m, n):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    for i in range(m - 1):
        head = head.next
        current = current.next
    for i in range(n - m):
        tmp = head.next
        head.next = tmp.next
        tmp.next = current.next
        current.next = tmp
    return dummy.next
    
