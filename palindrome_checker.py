import unittest
from palindrome_checker import is_palindrome

class TestPalindrome(unittest.TestCase):

    def test_known_palindromes(self):
        self.assertTrue(is_palindrome("А роза упала на лапу Азора"))
        self.assertTrue(is_palindrome("Madam"))
        self.assertTrue(is_palindrome("Never odd or even"))
        self.assertTrue(is_palindrome("radar"))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("race a car"))  # "raceacar" != "racacear"

    def test_edge_cases(self):
        self.assertTrue(is_palindrome(""))      # пустая строка
        self.assertTrue(is_palindrome("a"))     # один символ
        self.assertTrue(is_palindrome("   "))   # только пробелы (после очистки – пустая)
        self.assertFalse(is_palindrome("ab"))   # не палиндром

    def test_case_and_spaces(self):
        self.assertTrue(is_palindrome("   A    "))   # после очистки "a"
        self.assertTrue(is_palindrome("A man a plan a canal panama"))

if __name__ == "__main__":
    unittest.main()
