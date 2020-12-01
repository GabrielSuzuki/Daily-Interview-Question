#Hi, here's your problem today. This problem was recently asked by Uber:

#Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a2 + b2 = c2

#Example:
#Input: [3, 5, 12, 5, 13]
#Output: True
#Here, 52 + 122 = 132.
def findPythagoreanTriplets(nums):
  # Fill this in.
  i = 0
  while i < len(nums) - 1:
    c = nums[i]
    j = i + 1
    if(j > len(nums) - 1):
      j = i - len(nums)
    k = i + 2
    if(k > len(nums) - 1):
      k = i - len(nums) + 1
    while j < len(nums) - 2:
      if(nums[k] == len(nums) - 1):
        j += 1
        if(j > len(nums) - 1):
          j = i - len(nums)
      k += 1
      if(k > len(nums) - 1):
          k = i - len(nums) + 1
      a = nums[j]
      b = nums[k]
      if(c * c == a * a + b * b):
        return True
    i += 1
  return False


print(findPythagoreanTriplets([3, 12, 5, 13]))
# True
