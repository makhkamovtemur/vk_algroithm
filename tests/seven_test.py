import sys
sys.path.append('../tasks/')

from seven_middle_node import *
import unittest

class TestFindMiddle(unittest.TestCase):
    def setUp(self):
        # Создание списка для тестирования
        self.nodes = [ListNode(i) for i in range(1, 6)]  # 1 -> 2 -> 3 -> 4 -> 5
        for i in range(len(self.nodes) - 1):
            self.nodes[i].next = self.nodes[i + 1]
        self.head = self.nodes[0]

    def test_find_middle_odd(self):
        middle = find_middle(self.head)
        self.assertEqual(middle.value, 3)

    def test_find_middle_even(self):
        # Добавляем еще один узел для создания списка с четным количеством узлов
        self.nodes[-1].next = ListNode(6)  # 1 -> 2 -> 3 -> 4 -> 5 -> 6
        middle = find_middle(self.head)
        self.assertEqual(middle.value, 4)

    def test_single_node(self):
        single_node = ListNode(1)
        self.assertEqual(find_middle(single_node).value, 1)

    def test_two_nodes(self):
        head = ListNode(1)
        head.next = ListNode(2)
        self.assertEqual(find_middle(head).value, 2)

if __name__ == '__main__':
    unittest.main()
