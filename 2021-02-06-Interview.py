#Hi, here's your problem today. This problem was recently asked by AirBNB:

#Given a sorted list of positive numbers, find the smallest positive number that cannot be a sum of any subset in the list.

#Example:
#Input: [1, 2, 3, 8, 9, 10]
#Output: 7
#Numbers 1 to 6 can all be summed by a subset of the list of numbers, but 7 cannot.
def findSmallest(nums):
  i = 0
  j = 0
  hit = False
  sums = 0
  templist = []
  while i < len(nums):
    #print(nums[i])
    templist.append(nums[i])
    j = i + 1
    while j < len(nums):
      sums += nums[i]
      templist.append(nums[j] + nums[i])
      templist.append(sums)
      j += 1
    i += 1
    sums = 0
  i = 1

  while i < nums[len(nums) - 1]:
    j = 0
    while(j < len(templist)):
      if(templist[j] == i):
        hit = True
        i += 1
        j = len(templist) 
      j += 1
    if(hit == False):
      return i
    else:
      hit = False
    i += 1

  # Fill this in.

print(findSmallest([1, 2, 3, 8, 9, 10]))
# 7
