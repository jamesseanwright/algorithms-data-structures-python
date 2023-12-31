import unittest
from a_basic_data_structures.stack import Stack

class TestStack(unittest.TestCase):
    def testWithBookExample(self):
        s = Stack()

        self.assertTrue(s.isEmpty())

        s.push(4)
        s.push("dog")

        self.assertEqual(s.peek(), "dog")

        s.push(True)

        self.assertEqual(s.size(), 3)
        self.assertFalse(s.isEmpty())

        s.push(8.4)

        self.assertEqual(s.pop(), 8.4)
        self.assertTrue(s.pop())
        self.assertEqual(s.size(), 2)