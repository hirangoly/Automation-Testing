import unittest
import sentenceHandling as sh

class SentenceHandlingTest(unittest.TestCase):
    '''test cases for break words'''
    
    def test_break_word(self):
        sentence = 'Hello This is Rangoly'
        words = ['Hello', 'This', 'is', 'Rangoly']
        words1 = ['hello', 'This', 'is', 'Rangoly']
        self.assertEqual(sh.break_words(sentence), words)
        self.assertNotEqual(sh.break_words(sentence), words1)
        
    def test_sorted_words(self):
        words = ['Hello', 'This', 'is', 'Rangoly']
        sorted_words = ['Hello', 'Rangoly', 'This', 'is']
        self.assertEqual(sh.sorted_words(words), sorted_words)
        
    def test_first_word(self):
        words = ['Hello', 'This', 'is', 'Rangoly']
        first_word = 'Hello'
        first_word1 = 'hello'
        self.assertEqual(sh.first_word(words), first_word)
        self.assertNotEqual(sh.first_word(words), first_word1)
    
    def test_last_word(self):
        words = ['Hello', 'This', 'is', 'Rangoly']
        last_word = 'Rangoly'
        last_word1 = 'rangoly'
        self.assertEqual(sh.last_word(words), last_word)
        self.assertNotEqual(sh.last_word(words), last_word1)
    
    def test_first_last_word_sentence(self):
        sentence = 'Hello This is Rangoly'
        first_word = 'Hello'
        last_word = 'Rangoly'
        self.assertEqual(sh.first_last_word_sentence(sentence), (first_word, last_word))
        
    def test_first_last_word_sorted_sentence(self):
        sentence = 'Hello This is Rangoly'
        first_sorted_word = 'Hello'
        last_sorted_word = 'is'
        self.assertEqual(sh.first_last_sorted_word_sentence(sentence), (first_sorted_word, last_sorted_word))
        
if __name__ == '__main__':
    unittest.main()
