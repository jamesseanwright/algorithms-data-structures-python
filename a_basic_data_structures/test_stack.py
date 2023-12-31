import unittest
from a_basic_data_structures.stack import Stack


class TestStack(unittest.TestCase):
    def test_with_book_example(self):
        s = Stack()

        self.assertTrue(s.is_empty())

        s.push(4)
        s.push("dog")

        self.assertEqual(s.peek(), "dog")

        s.push(True)

        self.assertEqual(s.size(), 3)
        self.assertFalse(s.is_empty())

        s.push(8.4)

        self.assertEqual(s.pop(), 8.4)
        self.assertTrue(s.pop())
        self.assertEqual(s.size(), 2)
