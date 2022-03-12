from collections import queue
from typing import Deque, List, FrozenSet



from string import ascii_lowercase

# Initialize chains: {"cat-dog" : [["cat","cot","cog","dog"],["cat",...,"dog"]], ...}
chains = {}

# Save word list to a list
wordlist = list(open("wordlist.txt").read().split())

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
        print("Current chain: ", chain)
        return

    # Find variants of word by changing one letter at a time
    for i in range(len(word)):
        for letter in ascii_lowercase:
            variant = word[:i] + letter + word[i+1:]
            if variant in wordlist and variant not in chain:
                chain.append(variant)
                find_chain(start_word, end_word, chain)

    # No chains found    
    return

find_chain("truck","whine")