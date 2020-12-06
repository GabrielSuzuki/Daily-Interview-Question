#Hi, here's your problem today. This problem was recently asked by Amazon:

#Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

#Example:
#Input: s = 7, nums = [2,3,1,2,4,3]
#Output: 2
#Explanation: the subarray [4,3] has the minimal length under the problem constraint.

#Here is the method signature:
class Solution:
  def minSubArrayLen(self, nums, s):
    maxsteps = 0
    for i in nums:
      k = i + 1
      total = nums[i]
      steps = 1
      while k < len(nums):
        total += nums[k]
        steps += 1
        if(total >= s):
          if(maxsteps == 0):
            maxsteps = steps
          elif(steps < maxsteps):
            maxsteps = steps
          k = len(nums)     
        k += 1
    return maxsteps



print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2


