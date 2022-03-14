from string import ascii_lowercase
from itertools import combinations
import random

# Initialize chains: {"cat-dog" : [["cat","cot","cog","dog"],["cat",...,"dog"]], ...}
chains = {}

debug = False
if debug:
    filename = "word_lists/wordlist2.txt"
    start = "ab"
    end = "be"
    alphabet = "abcde"
else:
    filename = "word_lists/wordlist.txt"
    start = "skate"
    end = "share"
    alphabet = ascii_lowercase

# Save word list to a list
wordlist = list(open(filename).read().split())
MAXLEN = 6

# TODO: ANKI
# wordlist = []
# filename = "wordlist.txt"
#with open(filename, 'r') as file:
#    for line in file:
#        filename.append(line.strip())


def find_chain(start_word, end_word, chain=[]):

    if not chain:
        chain.append(start_word)
    
    word = chain[-1]

    # Base case: "start_word-end_word" chain found
    if word == end_word:
        
        key = start_word + "-" + end_word
        if not chains.get(key):
            chains[key] = [chain]
        else:
            chains[key].append(chain)
        print("Chain found! ", chain)
        chain = chain[:-1]
        return chain
    
    if len(chain) > MAXLEN:
        chain = chain[:-1]
        return chain

    # Find variants of word by changing one letter at a time
    for i in range(len(word)):
        for letter in alphabet:
            variant = word[:i] + letter + word[i+1:]
            print(f"Variant: {variant}, Chain: {chain}")
            if variant in wordlist and variant not in chain:
                chain.append(variant)
                chain = find_chain(start_word, end_word, chain)

    # No chains found
    chain = chain[:-1]    
    return chain


def random_chain():

    wordlist_selected = list(open("word_lists/wordlist_selected.txt").read().split())

    start, end = random.sample(wordlist, 2)
    print(f"Start word: {start}")
    print(f"End word: {end}")
    find_chain(start,end)

random_chain()