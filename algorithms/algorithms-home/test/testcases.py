import unittest
<<<<<<< HEAD
from algorithms import one_edit, look_and_say


class TestCases(unittest.TestCase):

    def test_is_one_edit(self):
        one_edit_test_cases = [("this", "thas", True),
                               ("tais", "this", True),
                               ("tabs", "this", False),
                               ("thisaa", "this", False),
                               ("aathis", "this", False),
                               ("thisa", "this", True),
                               ("athis", "this", True),
                               ("tahis", "this", True),
                               ("thaeis", "this", False),
                               ("tish", "this", False)
                               ]
        for w1, w2, res in one_edit_test_cases:
            try:
                self.assertTrue(one_edit.is_one_edit(w1, w2) == res)
            except AssertionError:
                print("%s wasn't one edit away from %s" % (w1, w2))
                raise AssertionError

    def test_look_and_say(self):
        test_cases = [(1, 11),
                      (11, 21),
                      (21, 1211),
                      (1211, 111221)]
        for input, output in test_cases:
            try:
                self.assertTrue(look_and_say.get_say(input) == output)
            except AssertionError:
                print("%s wasn't equal to output %s" % (input, output))
                raise AssertionError

=======
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
>>>>>>> 9ea909b80258d6d2b5e4b1c569face871dfe090d
