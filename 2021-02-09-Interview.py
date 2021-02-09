#Hi, here's your problem today. This problem was recently asked by Amazon:

#You are given an array of integers. Return the length of the longest consecutive elements sequence in the array.

#For example, the input array [100, 4, 200, 1, 3, 2] has the longest consecutive sequence 1, 2, 3, 4, and thus, you should return its length, 4.
def longest_consecutive(nums):
  i = 0
  j = 0
  k = 0
  temp = 0
  tempmax = 1
  total = 0 
  while i < len(nums):
    j = i + 1
    k = 0
    temp = nums[i] + 1
    if(j == len(nums)):
      j = 0
    while(k < len(nums)):
      if(temp == nums[j]):
        temp = nums[j] + 1
        tempmax += 1
      j += 1
      k += 1
      if(j == len(nums)):
        j = 0
    if(total < tempmax):
      total = tempmax
    i += 1
  return total
  # Fill this in.

print(longest_consecutive([100, 4, 200, 1, 3, 2]))
# 4
