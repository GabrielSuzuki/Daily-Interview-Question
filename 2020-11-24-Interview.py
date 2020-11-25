#Hi, here's your problem today. This problem was recently asked by Facebook:

#You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

#Example:
#Given [4, 7, 1 , -3, 2] and k = 5, 
#return true since 4 + 1 = 5.
def two_sum(list, k):
  j = 1
  i = 0
  while i < len(list):
    if((j == len(list)) and (len(list) == 2)):
      return False
    if(list[i]+ list[j] == k):
      return True
    else:
      if(j >= (len(list) - 1)):
        i += 1
        j = i + 1
      else:
        j += 1
  return False     
  

print(two_sum([3,1,4,1], 5))
# True

#Try to do it in a single pass of the list.
