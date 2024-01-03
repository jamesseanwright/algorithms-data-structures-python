import unittest

from a_basic_data_structures.base_n import unsigned_dec_to_base_n


class TestBaseN(unittest.TestCase):
    def test_unsigned_dec_to_base_n_returns_binary_when_no_base_provided(self):
        self.assertEqual(unsigned_dec_to_base_n(186), "10111010")
        self.assertEqual(unsigned_dec_to_base_n(255), "11111111")
        self.assertEqual(unsigned_dec_to_base_n(5), "101")

    def test_unsigned_dec_to_base_n_returns_octal_when_base_8_provided(self):
        self.assertEqual(unsigned_dec_to_base_n(2024, 8), "3750")
        self.assertEqual(unsigned_dec_to_base_n(8, 8), "10")
        self.assertEqual(unsigned_dec_to_base_n(511, 8), "777")

    def test_unsigned_dec_to_base_n_returns_hex_when_base_16_provided(self):
        self.assertEqual(unsigned_dec_to_base_n(15, 16), "F")
        self.assertEqual(unsigned_dec_to_base_n(8000, 16), "1F40")
        self.assertEqual(unsigned_dec_to_base_n(11259375, 16), "ABCDEF")
