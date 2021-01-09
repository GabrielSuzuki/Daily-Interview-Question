#Hi, here's your problem today. This problem was recently asked by AirBNB:

#Given a list of words, group the words that are anagrams of each other. (An anagram are words made up of the same letters).

#Example:

#Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
#Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]

#Here's a starting point:
import collections

def groupAnagramWords(strs):
  i = 0
  j = 0
  first = ""
  second = ""
  temp1 = ""
  temp2 = ""
  temparray = []
  finalarray = []
  removearray = []
  while i < len(strs):
    j = i + 1
    first = strs[i]
    temparray.append(first)
    while j < len(strs):
      second = strs[j]
      temp1 = sorted(first)
      temp2 = sorted(second)
      if(temp1 == temp2):
        temparray.append(second)
        removearray.append(j)
      j += 1
    for k in removearray:
      strs.remove(strs[k])
    removearray = []
    finalarray.append(temparray)
    temparray = []
    i += 1
  return finalarray

    

  # Fill this in.

print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]
