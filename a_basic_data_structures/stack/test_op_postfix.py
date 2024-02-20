import unittest
from a_basic_data_structures.stack.op_postfix import to_postfix


class TestToPostfix(unittest.TestCase):
    def test_to_postfix_converts_infix_expression_to_postfix(self):
        self.assertEqual(to_postfix("(A + B) * C"), "A B + C *")
        self.assertEqual(to_postfix("A + B * C + D"), "A B C * + D +")
        self.assertEqual(to_postfix("(A + B) * (C + D)"), "A B + C D + *")
