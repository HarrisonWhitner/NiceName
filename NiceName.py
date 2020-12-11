#!/usr/bin/env python3

import sys
import doctest
from jellyfish import jaro_winkler_similarity

""" 
NiceName
A python package for detecting offensive usernames

Note: Usernames are assumed to be 25 

Authors: Harrison Whitner, Jeremy Howe
Creation Date: 11/28/20
"""

""" CONSTANTS """

BAD_WORD_LIST_FILEPATH = 'bad_words_cmu.txt' #TODO switch to the master and combine the bad word files
LEETSPEAK_TO_ENGLISH_DICT = {'0':'o',
                             '1':'l',
                             '3':'e', 
                             '4':'a', 
                             '5':'s', #TODO handle alternate 5 -> h translation
                             '7':'t', #TODO handle x -> k translation
                             '8':'b', 
                             '!':'i',
                             '@':'a',
                             '$':'s',
                             '+':'t'}

""" FUNCTIONS """

def score_username(usr: str, debug=False) -> float:
    """ Returns a score for a username between 0 and 1, 0 being surely inoffensive and 1 being surely offensive.
    """

    # check for empty paramter
    if not usr:
        raise ValueError('Missing username arguement')

    # loads bad word list
    bad_words = None
    with open(BAD_WORD_LIST_FILEPATH, 'r') as fp:
        bad_words = set([w[:-2] for w in list(fp) if len(w[:-2]) > 0]) # remove the last 2 characters which are always a newline '\n'

    # preprocess username
    processed_usr = preprocess_username(usr)

    # check if the whole username is match for any in the bad list, return a strong bad score if so

    # if max score is above a threshold, return 

    # parse name for recognizable word, preferring the longest possible ones

    # check if any words are in the bad list, return a strong bad score if so

    # check every combination of words with leftover adjacent text against bad list using soundex and jaro-winkler distance

    # check versions with numbers replaced with similar letters (leetspeak check)

    # return the largest score of the word combinations
    
    return 0.5

def preprocess_username(usr: str, debug=False) -> str:
    """ Prepares a word for scanning by removing characters outside of alphanumeric characters and forcing all lowerspace.
    """
    
    #TODO remove all non-alphanumeric characters
    
    # convert to all lowercase characters
    usr = usr.lower()

    return usr

def score_word(seg: str, debug=False) -> float:
    """ Returns a score for a word between 0 and 1, 0 being surely inoffensive and 1 being surely offensive. 
    """
    
    # create a list of possible leetspeak translations of the word, along with the original word

    # loop through all the bad words in the list

        # compare all target words against current bad word with jaro winkler, store greatest score

    # return the greatest score of all comparisions

    return 0.5

def leetspeak_to_english(seg: str, debug=False) -> list:
    """ Returns a list of strings with all non-alphabetic character replaced by similar looking alphabetic characters.
    
    NOTE: This returns a list of strings to consider multiple possible translations of characters, but that functionality is not currently implemented.

    >>> leetspeak_to_english('41ph483+')
    ['alphabet']

    >>> leetspeak_to_english('8ad@$$g00n')
    ['badassgoon']

    >>> leetspeak_to_english('normaltestwoowoo')
    ['normaltestwoowoo']

    >>> leetspeak_to_english('8!+ch')
    ['bitch']
    """

    translations = ['']

    for char in seg:
        
        if char in LEETSPEAK_TO_ENGLISH_DICT:
            translations[0] += LEETSPEAK_TO_ENGLISH_DICT[char]
        
        else:
            translations[0] += char
    
    return translations


""" MAIN GUARD """

if __name__ == '__main__':

    # get a username if not provided by arguement
    if len(sys.argv) < 2:
        cur_username = input('Please enter a username to score: ')

    # check if the user is running a doctest
    elif sys.argv[1] == 'doctest':
        doctest.testmod()
        exit()

    # get the username from the arguements passed
    else:
        cur_username = sys.argv[1]

    # score the provided username
    cur_score = score_username(cur_username)
    print('Score calculated for the username above:', str(cur_score))