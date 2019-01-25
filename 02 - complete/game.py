#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    letters = []
    for i in range(NUM_LETTERS):
        draw = random.choice(POUCH)
        POUCH.remove(draw)
        letters.append(draw)
    return letters

def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    word = input('Form a valid word:')
    while _validation(word,draw) == False:
        word = input("Invalid word. Form a valid word:")
    else:
        return word




def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    if word in DICTIONARY:
        # process and sort
        word = list(word.upper())
        word.sort()
        draw.sort()

        # compare two lists
        j = 0
        for i in range(len(draw)):
            # print(i,j)
            if draw[i] == word[j]: # if letter matches, go next letter
                j+=1
                if j == len(word): # if end of word, return True
                    return True
                continue
    else:
        raise ValueError("Not valid entry.")

# while (_validation('weave',['v','e','e','w','a','o','s']))


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    possible_words = _get_permutations_draw(draw)
    '''new_list =[]
    for word in possible_words:
        if word in DICTIONARY:
            new_list.append(word)
    print(new_list)
    return(new_list)'''
    return(set(possible_words) & set(DICTIONARY)) # intersection



def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    perm_list = []
    for i in range(1,len(draw)+1):
        for permutation in list(itertools.permutations(draw,i)):
            perm_list.append(permutation)
    new_list = []
    for word in perm_list:
        word = ''.join(word).lower()
        new_list.append(word)
    return new_list


# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
