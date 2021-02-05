#Hi, here's your problem today. This problem was recently asked by Uber:

#Given a number of integers, combine them so it would create the largest number.

#Example:
#Input:  [17, 7, 2, 45, 72]
#Output:  77245217
def largestNum(nums):
  biggest = 0
  fullbiggest = 0
  biggestpos = 0
  i = 0
  j = 0
  tempstring = ""
  fulllength = len(nums)
  while(fulllength > j):
    biggest = 0 
    while i < len(nums):
      k = nums[i]
      while(k > 9):
        k /= 10
      if(k > biggest):
        biggest = k
        fullbiggest = nums[i]
        biggestpos = i
      i += 1
    tempstring += str(fullbiggest)
    nums.pop(biggestpos)
    i = 0
    j += 1
  return tempstring



    
  # Fill this in

print(largestNum([17, 7, 2, 45, 72]))
# 77245217
