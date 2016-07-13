# print break words
def break_words(sentence):
    words = sentence.split(' ')
    return words
    
# print sorted words 
def sorted_words(words):
    return sorted(words)

# print first word of a sentence
def first_word(words):
    word = words.pop(0)
    return word
    
# print last word of a sentence
def last_word(words):
    word = words.pop(-1)
    return word
    
# print sorted sentence
def sorted_sentence(sentence):
    words = break_words(sentence)
    return sorted_words(words)
    
# print first and last word of sentence
def first_last_word_sentence(sentence):
    words = break_words(sentence)
    word1 = first_word(words)
    word2 = last_word(words)
    return word1, word2

# print first and last word of senetence after sorting
def first_last_sorted_word_sentence(sentence):
    words = sorted_sentence(sentence)
    word1 = first_word(words)
    word2 = last_word(words)
    return word1, word2
