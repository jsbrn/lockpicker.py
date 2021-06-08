import re
import sys

print("Loading words and letters...")

# Load from given list of words (ex. dicts/popular.txt)
# See dicts folder for some useful sets

with open(sys.argv[1]) as f:
    words = set(f.readlines())

# Put all attempted words into attempts.txt and they will be ignored by the result

with open('attempts.txt') as f2:
    attempts = set(f2.readlines())

words = words - attempts

# Load the lock configuration

with open('lock.txt') as f3:
    letters = f3.readlines()

f.close()
f2.close()

dictionary = []
found_words = []

print("Collecting all valid words...")

# For each loaded word, check if it is 4 characters long and each character is available on the corresponding lock wheel/slot
# If so, then add it to found words

for word in words:
    word = word.strip().lower()
    valid = len(word) == len(letters)
    if valid:
        word_chars = list(word)
        slot = 0
        for char in word_chars:
            if char not in letters[slot].lower():
                valid = False
                break
            slot = slot + 1
    if valid == True:
        found_words.append(word)

print("Done!")
print(found_words)
print("Found " + str(len(found_words)) + " valid words!")

# Output all found words in printable format
# So you can take the list with you

result_string = ""
for word in found_words:
    result_string = result_string + word + " "

with open("printable.txt", "w") as w:
    w.write(result_string.strip())
    w.close()