# palidrome_check_unittest
import palindrome_check as pc
import unittest

class PalindromeCheck(unittest.TestCase):
     
    def test_valid_string(self):
        valid_palindrome = 'A man a plan a canal Panama'
        self.assertTrue(pc.check_palindrome(valid_palindrome))
        
    def test_invalid_string(self):
        invalid_palindrome = 'race a car'
        self.assertFalse(pc.check_palindrome(invalid_palindrome))
        
if __name__ == '__main__':
    unittest.main()
