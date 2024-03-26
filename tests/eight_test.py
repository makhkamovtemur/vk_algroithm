import sys
sys.path.append('../tasks/')

from eight_remove_node import *
import unittest

class TestRemoveNode(unittest.TestCase):
    def list_to_values(self, head):
        """Преобразует список в массив значений для удобства проверки."""
        values = []
        while head:
            values.append(head.value)
            head = head.next
        return values

    def test_remove_middle_node(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        head = remove_node(head, 2)
        self.assertEqual(self.list_to_values(head), [1, 3])

    def test_remove_first_node(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        head = remove_node(head, 1)
        self.assertEqual(self.list_to_values(head), [2, 3])

    def test_remove_last_node(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        head = remove_node(head, 3)
        self.assertEqual(self.list_to_values(head), [1, 2])

    def test_remove_node_not_present(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        head = remove_node(head, 4)
        self.assertEqual(self.list_to_values(head), [1, 2, 3])

    def test_remove_multiple_nodes(self):
        head = ListNode(1, ListNode(2, ListNode(2, ListNode(3))))
        head = remove_node(head, 2)
        self.assertEqual(self.list_to_values(head), [1, 3])

if __name__ == '__main__':
    unittest.main()
