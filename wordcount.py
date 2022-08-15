"""Count words in file.
As I was going to St. Ives
I met a man with seven wives
Every wife had seven sacks
Every sack had seven cats
Every cat had seven kits
Kits, cats, sacks, wives.
How many were going to St. Ives?

"""
import sys

# def le_words(file_name):
#   file = open(file_name)

#   count_words = {}

#   for line in file:
#     line = line.rstrip()
#     line = line.split(" ")
#     for word in line:
#         count_words[word] = count_words.get(word, 0) + 1 
#   print(count_words)
# le_words(sys.argv[1])

def tokenize(file_name):
  file = open(file_name)
  words = []
  for line in file:
    line = line.rstrip()
    line = line.split(" ")
    for word in line:
      words.append(word)
  return words
print(tokenize("test.txt")) 

def normalize_text(words):
  punctuation = [",", "!", ".", "?"]
  new_words = []
  for word in words:
    word = word.lower()
    for pun in punctuation:
      if pun in word: 
        word = word[:-1]
    new_words.append(word)
  return new_words



def count_words(words):
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1 
    return count
print(count_words(tokenize("test.txt")))

def print_words_count(word_counts):
  for key in word_counts:
    print(key, word_counts[key])
    
print_words_count(count_words(normalize_text(tokenize("test.txt"))))