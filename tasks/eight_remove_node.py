class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_node(head, val):
    dummy = ListNode(0)  # Фиктивный узел для упрощения удаления узла в начале списка
    dummy.next = head
    current = dummy
    while current.next:
        if current.next.value == val:
            current.next = current.next.next
        else:
            current = current.next
    return dummy.next