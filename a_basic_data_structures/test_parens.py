import unittest
from a_basic_data_structures.parens import is_balanced


class TestParens(unittest.TestCase):
    def test_is_balanced_returns_true_when_parens_are_balanced(self):
        self.assertTrue(is_balanced("(() () () ())"))
        self.assertTrue(is_balanced("(((())))"))
        self.assertTrue(is_balanced("(()((())()))"))

    def test_is_balanced_returns_false_when_parens_are_not_balanced(self):
        self.assertFalse(is_balanced("((((((())"))
        self.assertFalse(is_balanced("()))"))
        self.assertFalse(is_balanced("(()()(()"))

    def test_is_balanced_returns_true_when_additional_symbols_are_balanced(self):
        self.assertTrue(is_balanced("{ { ( [ ] [ ] ) } ( ) }"))
        self.assertTrue(is_balanced("[ [ { { ( ( ) ) } } ] ]"))
        self.assertTrue(is_balanced("[ ] [ ] [ ] ( ) { }"))

    def test_is_balanced_returns_false_when_additional_symbols_are_not_balanced(self):
        self.assertFalse(is_balanced("( [ ) ]"))
        self.assertFalse(is_balanced("( ( ( ) ] ) )"))
        self.assertFalse(is_balanced("[ { ( ) ]"))
