#Hi, here's your problem today. This problem was recently asked by Twitter:

#You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.

#Example:

#[34, -50, 42, 14, -5, 86]

#Given this input array, the output should be 137. The contiguous subarray with the largest sum is [42, 14, -5, 86].

#Your solution should run in linear time.

#Here's a starting point:
def max_subarray_sum(arr):
  i = 0
  k = 0
  tempsum = 0
  totalsum = 0
  while i < len(arr):
    tempsum += arr[i]
    i += 1
    if tempsum > totalsum:
      totalsum = tempsum
    if(i == len(arr) and k < len(arr)):
      k += 1
      i = k
      tempsum = 0
  return totalsum
  # loop through the array 
  # move to next spot
  # make a greatest sum
  # if it is greater than that sum replace it

print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137
