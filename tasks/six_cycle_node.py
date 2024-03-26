class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def is_cyclic(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
