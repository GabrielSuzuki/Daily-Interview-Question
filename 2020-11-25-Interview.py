#Hi, here's your problem today. This problem was recently asked by Facebook:

#Given a list of numbers, where every number shows up twice except for one number, find that one number.

#Example:
#Input: [4, 3, 2, 4, 1, 3, 2]
#Output: 1
#Here's the function signature:
def singleNumber(nums):
  #j = 1
  #i = 0
  #while i < len(nums):
    #if(nums[i] = nums[j]):
      #i += 1
    #else:
     # if(j == len(nums)):

     # j += 1
  

  #xor
  res = nums[0]
  for i in range(1,len(nums)):
    res = res ^ nums[i]
  return res
       
    

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1

#Challenge: Find a way to do this using O(1) memory.
