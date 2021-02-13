#Hi, here's your problem today. This problem was recently asked by Apple:

#You are given two strings, A and B. Return whether A can be shifted some number of times to get B.

#Eg. A = abcde, B = cdeab should return true because A can be shifted 3 times to the right to get B. A = abc and B= acb should return false.
def is_shifted(a, b):
  i = 0
  j = 0
  k = 0
  tempstring = ""
  while i < len(a):
    tempstring = ""
    j = i + 1
    k = 0
    if(j == len(a)):
      j = 0
    while k < len(a):
      if(j == len(a)):
        j = 0
      tempstring += a[j]
      j += 1
      k += 1
    if(tempstring == b):
      return True
    i += 1
  return False

  # Fill this in.
  
print(is_shifted('abcde', 'cdeab'))
# True
