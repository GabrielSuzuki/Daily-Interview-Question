#Hi, here's your problem today. This problem was recently asked by Twitter:

#Given a list of integers, return the bounds of the minimum range that must be sorted so that the whole list would be sorted.

#Example:
#Input: [1, 7, 9, 5, 7, 8, 10]
#Output: (1, 5)
#Explanation:
#The numbers between index 1 and 5 are out of order and need to be sorted.

#Here's your starting point:
def findRange(nums):
  i = 0
  pos = 1
  firstpos = 0
  firstbool = False
  while i < len(nums):
    j = i + 1
    while j < len(nums):
      if(nums[i] > nums[j]):
        pos += 1
        firstbool = True
      else:  
        if(firstbool == False):
          firstpos = i
      j += 1
    i += 1
  return (firstpos,pos)

  # Fill this in.

print(findRange([1, 7, 9, 5, 7, 8, 10]))
# (1, 5)
