import re

start_word = "MAGIC"
end_word = "BUGLE"
word_length = re.compile('.{' + str(len(start_word)) + '}(\n)?$', re.I)
filename = "wordlist.txt"

with open(filename, 'r') as f:
    words = set(word.strip().upper() for word in f if re.match(word_length, word))