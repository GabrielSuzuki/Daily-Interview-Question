#Hi, here's your problem today. This problem was recently asked by Facebook:

#Two words can be 'chained' if the last character of the first word is the same as the first character of the second word. 

#Given a list of words, determine if there is a way to 'chain' all the words in a circle.

#Example:
#Input: ['eggs', 'karat', 'apple', 'snack', 'tuna']
#Output: True
#Explanation:
#The words in the order of ['apple', 'eggs', 'snack', 'karat', 'tuna'] creates a circle of chained words.

#Here's a start:
from collections import defaultdict
def chainedWords(words):
  boolfirst = False
  first = ""
  tempfirst = "" 
  last = ""
  i = 0
  while i < len(words):
    if(boolfirst == False):
      boolfirst = True
      first = words[i][0]
    last = words[i][len(words[i]) - 1]
    if(i == len(words) - 1):
      if(last == first):
        return True
    j = i + 1
    while j < len(words):
      tempfirst = words[j][0]
      if(tempfirst == last):
        break
      else:
        j += 1
      if(j == len(words)):
        return False
    i += 1


print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))
# True
