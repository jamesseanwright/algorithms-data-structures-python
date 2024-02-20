import unittest
from a_basic_data_structures.stack.eval_postfix_expr import eval_postfix_expr


class TestEvalPostfixExpr(unittest.TestCase):
    def test_eval_postfix_expr_correctly_evaluates_expr(self):
        self.assertEqual(eval_postfix_expr("4 5 6 * +"), 34)
        self.assertEqual(eval_postfix_expr("7 8 + 3 2 + /"), 3)

    def test_eval_postfix_expr_raises_exception_on_invalid_token(self):
        self.assertRaises(ValueError, lambda: eval_postfix_expr("X 7 +"))
