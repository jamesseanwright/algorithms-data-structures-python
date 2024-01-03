import unittest

from a_basic_data_structures.base_n import dec_to_base_n


class TestBaseN(unittest.TestCase):
    def test_dec_to_base_n_returns_binary_when_no_base_provided(self):
        self.assertEqual(dec_to_base_n(186), "10111010")
        self.assertEqual(dec_to_base_n(255), "11111111")
        self.assertEqual(dec_to_base_n(5), "101")
