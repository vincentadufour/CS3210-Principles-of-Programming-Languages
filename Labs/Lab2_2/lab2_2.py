from collections import defaultdict
import re
from functools import reduce

def read_words_from_file(filename):
    """Reads words from a file, removes punctuation, and returns a list of words."""
    with open(filename, 'r') as file:
        text = file.read().lower()  # Convert to lowercase for case-insensitive counting

        # Remove punctuation using regular expressions
        text = re.sub(r'[^\w\s]', '', text)
        return text.split()

def count_word_occurrences(words):
    """Counts occurrences of each word using a dictionary."""
    word_count = defaultdict(int)  # Dictionary to store word counts
    # Loop through each word and update its count

    for word in words:
        word_count[word] += 1

    return word_count

# Using Functions
def count_words(word):    
    words_dict = {}
    words_dict[word] = 1

    return words_dict

def group(word_count, new_word_count):

    for word, count, in new_word_count.items():
        word_count[word] = word_count.get(word, 0) + count

    return word_count
    

filename = '/home/vincent/Documents/MSUDenver/CS3210/Labs/Lab2_2/words.txt'  # Replace with the path to your file

words = read_words_from_file(filename)

word_count_mapped = list(map(lambda x: count_words(x), words))

word_count = reduce(group, word_count_mapped, {})

print(word_count)
