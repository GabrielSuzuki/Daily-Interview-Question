#Hi, here's your problem today. This problem was recently asked by Amazon:

#Given two arrays, write a function to compute their intersection - the intersection means the numbers that are in both arrays.

#Example 1:
#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2]
#Example 2:
#Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#Output: [9,4]
#Note:
#Each element in the result must be unique.
#The result can be in any order.

#Here's a starting point:
class Solution:
  def intersection(self, nums1, nums2):
    k = 0
    i = 0
    temparray = []
    while i < len(nums1):
      while k < len(nums2):
        if nums1[i] == nums2[k]:
          temparray.append(nums1[i])
          k = 0
          break
        k += 1
      i += 1
    return temparray

    # Fill this in.

print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
# [9, 4]
