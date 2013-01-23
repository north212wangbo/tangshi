#!/usr/bin/python
#Author: Bo Wang
"""
This is a python program that mimic traditional Chinese poem.
The text file I provide is called 'puretangshi.txt', which is in utf-8 encoding.
If you want to try your own text, don't forget to convert it to utf-8.
To run the program in command line, type ./tangshimimic.py file-to-read, this will print out a constructured poem.
"""

import random
import sys
import re

def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++                                                                      
  dict = {}
  file = open(filename,"rU")
  text = file.read()
  long_string = text.decode('utf8') #decode the text
  file.close()
  words_list = []
  for i in range(len(long_string)):
    words_list.append(long_string[i])
  prev = ''

  for word in words_list: #create the dictionary
    if not prev in dict:
      dict[prev]=[word]
    else:
      dict[prev].append(word)
    prev = word
  return dict

def print_mimic(mimic_dict, word): #print the mimic poem
  """Given mimic dict and start word, prints mimic poem with four sentences, each seven words."""
                                                                      
  next_word = random.choice(mimic_dict[word])
  mimic_text = ''
  i = 0
  while i<7:
    if next_word in mimic_dict:
      next_word = random.choice(mimic_dict[next_word])
      next_word_utf8 = next_word.encode('utf8')
      
      match = re.search(ur"[\u4e00-\u9fa5]+",next_word)
      
      if match: 
        mimic_text += next_word
        i += 1
  mimic_text += '\n'

  next_word = random.choice(mimic_dict[word])
  i = 0
  while i<7:
    if next_word in mimic_dict:
      next_word = random.choice(mimic_dict[next_word])
      next_word_utf8 = next_word.encode('utf8')
      match = re.search(ur"[\u4e00-\u9fa5]+",next_word)
      if match: 
        mimic_text += next_word
        i += 1
  mimic_text += '\n'

  next_word = random.choice(mimic_dict[word])
  i = 0
  while i<7:
    if next_word in mimic_dict:
      next_word = random.choice(mimic_dict[next_word])
      next_word_utf8 = next_word.encode('utf8')
      match = re.search(ur"[\u4e00-\u9fa5]+",next_word)
      if match: 
        mimic_text += next_word
        i += 1
  mimic_text += '\n'

  next_word = random.choice(mimic_dict[word]) 
  i = 0
  while i<7:
    if next_word in mimic_dict:
      next_word = random.choice(mimic_dict[next_word])
      next_word_utf8 = next_word.encode('utf8')
      match = re.search(ur"[\u4e00-\u9fa5]+",next_word)
      if match: 
        mimic_text += next_word
        i += 1
  mimic_text += '\n'
  
  print mimic_text
  return


# Provided main(), calls mimic_dict() and mimic()                                             
def main():
  if len(sys.argv) != 2:
    print 'usage: ./tangshimimic.py file-to-read'
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')

if __name__ == '__main__':
  main()
