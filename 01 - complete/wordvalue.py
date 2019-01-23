from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        words_list = f.read().splitlines()
    return words_list

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for i in range(len(word)):
        if word[i].upper() in LETTER_SCORES.keys():
            score += LETTER_SCORES[word[i].upper()]
    return score

def max_word_value(words_list=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_word = ''
    for word in words_list:
        if calc_word_value(max_word) < calc_word_value(word):
            max_word = word
    return max_word


if __name__ == "__main__":
    pass # run unittests to validate
