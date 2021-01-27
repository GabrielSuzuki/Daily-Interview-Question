#Hi, here's your problem today. This problem was recently asked by Facebook:

#Starting at index 0, for an element n at index i, you are allowed to jump at most n indexes ahead. Given a list of numbers, find the minimum number of jumps to reach the end of the list.

#Example:
#Input: [3, 2, 5, 1, 1, 9, 3, 4]
#Output: 2
#Explanation:

#The minimum number of jumps to get to the end of the list is 2: 
#3 -> 5 -> 4

#Here's a starting point:
def jumpToEnd(nums):
  i = 0
  jumps = -1
  while i < len(nums):
    n = nums[i]
    i = n + i
    if(i > len(nums) - 1):
      return jumps
    else:
      jumps += 1
  return jumps


print(jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))
# 2
