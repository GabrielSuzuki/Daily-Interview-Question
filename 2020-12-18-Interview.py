#Hi, here's your problem today. This problem was recently asked by Microsoft:

#You are given an array of intervals - that is, an array of tuples (start, end). The array may not be sorted, and could contain overlapping intervals. Return another array where the overlapping intervals are merged.

#For example:
#[(1, 3), (5, 8), (4, 10), (20, 25)]

#This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).

#Here's a starting point:
def merge(intervals):
  #save 1 tuple
  #use 2nd tuple to check the first
  # if there is no 2nd tuple, just add the 1st tuple
  #check if 1stnum1 < 2ndnum1
    #if yes check if 1stnum2 < 2ndnum1
      #if yes add 1st to list
      #if no add (1stnum1,2ndnum2)
    #if no check if 1stnum2 < 2ndnum2
      #if yes add 2nd
      #if no add (2ndnum1,1stnum2)
  # Fill this in.
  
print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]
