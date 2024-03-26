import sys
sys.path.append('../tasks/')

from six_cycle_node import *
import unittest

class TestCyclicList(unittest.TestCase):
    def test_cyclic_list(self):
        # Создаем циклический список: 1 -> 2 -> 3 -> 4 -> 2 ...
        head = ListNode(1)
        second = ListNode(2)
        third = ListNode(3)
        fourth = ListNode(4)
        head.next = second
        second.next = third
        third.next = fourth
        fourth.next = second  # Создание цикла
        self.assertTrue(is_cyclic(head))

    def test_non_cyclic_list(self):
        # Создаем нециклический список: 1 -> 2 -> 3 -> 4
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        self.assertFalse(is_cyclic(head))

    def test_empty_list(self):
        # Проверяем пустой список
        self.assertFalse(is_cyclic(None))

    def test_one_element_list(self):
        # Проверяем список из одного элемента без цикла
        self.assertFalse(is_cyclic(ListNode(1)))

    def test_one_element_cyclic_list(self):
        # Проверяем список из одного элемента с циклом
        head = ListNode(1)
        head.next = head  # Создание цикла
        self.assertTrue(is_cyclic(head))

if __name__ == '__main__':
    unittest.main()
