import unittest
from algorithms import valid_parens, len_sorted_array

class TestCases(unittest.TestCase):

    def test_valid_parens(self):
        test_cases = [
            ("{}{}", True),
            ("}", False),
            ("")
        ]
        for input, output in test_cases:
            self.assertTrue(valid_parens.valid_parens(input) == output)


    def test_len_sorted_array(self):
        test_cases = [
            ([1,1,2,2,3,3,4,4], 4),
            ([1,2,3], 3),
            ([1], 1)
        ]
        for input, output in test_cases:
            self.assertTrue(len_sorted_array.len_sorted_array(input) == output)