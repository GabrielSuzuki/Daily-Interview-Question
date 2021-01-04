#Hi, here's your problem today. This problem was recently asked by Apple:

#Given a list of words, and an arbitrary alphabetical order, verify that the words are in order of the alphabetical order.

#Example:
#Input:
#words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"

#Output: False
#Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'

#Example 2:
#Input:
#words = ["zyx", "zyxw", "zyxwy"],
#order="zyxwvutsrqponmlkjihgfedcba"

#Output: True
#Explanation: The words are in increasing alphabetical order

#Here's a starting point:
def isSorted(words, order):
  phrase1 = words[0]
  phrase2 = words[1]
  smaller = ""
  first = 0
  second = 0
  i = 0
  j = 0
  if(len(phrase1) == len(phrase2)):
    smaller = phrase1
  elif(len(phrase1) > len(phrase2)):
    smaller = phrase2
  elif(len(phrase2) > len(phrase1)):
    smaller = phrase1
  while i < len(smaller):
    #need to check if the phrases are the same
    if(phrase1[i] == phrase2[i]):
      pass
    else:
      while j < len(order):
        if(phrase1[i] == order[j]):
          first = j
        if(phrase2[i] == order[j]):
          second = j
        j += 1
      if(first > second):
        return False
      elif(second > first):
        return True
    i += 1
  if(smaller == phrase1):
    return True
  else:
    return False

  # Fill this in.

print(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print(isSorted(["zyx", "zyxw", "zyxwy"],
               "zyxwvutsrqponmlkjihgfedcba"))
# True
