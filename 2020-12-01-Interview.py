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
      j = i - len(nums) #goes back to 0th position
    k = i + 2
    if(k > len(nums) - 1):#goes back to 1st position
      k = j - len(nums)
    while j < len(nums) - 1:# loops through j(right after i) to end of list
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
