import unittest
from third import count_letter_in_string

class TestCountLetterInString(unittest.TestCase):

    def test_input_not_string_return_0(self):
        result = count_letter_in_string(1235, 'a')
        self.assertEqual(0, result)

    def test_working_correct(self):
        result = count_letter_in_string('apple', 'p')
        self.assertEqual(2, result)

    def test_counting_number_is_not_correct(self):
        result = count_letter_in_string('apple1', '1')
        self.assertFalse(1, result)

    def test_counting_upper_and_lowercase_too(self):
        result = count_letter_in_string('Appeal', 'a')
        self.assertEqual(2, result)

if __name__ == '__main__':
    unittest.main()
