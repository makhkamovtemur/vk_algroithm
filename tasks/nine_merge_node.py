class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(list1, list2):
    dummy = ListNode(0)  # Фиктивный начальный узел
    tail = dummy

    while list1 and list2:
        if list1.value <= list2.value:
            tail.next, list1 = list1, list1.next
        else:
            tail.next, list2 = list2, list2.next
        tail = tail.next
    # Присоединяем оставшийся список
    tail.next = list1 or list2

    return dummy.next