#Hi, here's your problem today. This problem was recently asked by Twitter:

#Given an array of integers of size n, where all elements are between 1 and n inclusive, find all of the elements of [1, n] that do not appear in the array. Some numbers may appear more than once.

#Example:
#Input: [4,5,2,6,8,2,1,5]
#Output: [3,7]
def findDisappearedNumbers(nums):
  i = 0
  maximum = 0
  temparray = []
  while i < len(nums):
    if(maximum < nums[i]):
      maximum = nums[i]
    i += 1
  i = 1
  j = 0
  hits = False
  while i < maximum:
    hits = False
    j = 0
    while j < len(nums):
      if(nums[j] == i):
        hits = True
        break
      j += 1
    if(hits == False):
      temparray.append(i)
    i += 1
  return temparray
    # Fill this in.

nums = [4, 6, 2, 6, 7, 2, 1]
print(findDisappearedNumbers(nums))
# [3, 5]
