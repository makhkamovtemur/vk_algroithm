import sys
sys.path.append('../tasks/')

from nine_merge_node import *
import unittest

class TestMergeSortedLists(unittest.TestCase):
    def list_to_values(self, head):
        """Преобразует список в массив значений для удобства проверки."""
        values = []
        while head:
            values.append(head.value)
            head = head.next
        return values

    def test_merge_sorted_lists(self):
        list1 = ListNode(3, ListNode(6, ListNode(8)))
        list2 = ListNode(4, ListNode(7, ListNode(9, ListNode(11))))
        merged = merge_sorted_lists(list1, list2)
        self.assertEqual(self.list_to_values(merged), [3, 4, 6, 7, 8, 9, 11])

if __name__ == '__main__':
    unittest.main()
