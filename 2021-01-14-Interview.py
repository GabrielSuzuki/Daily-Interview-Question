#Hi, here's your problem today. This problem was recently asked by Amazon:

#You are given an array of integers. Return an array of the same size where the element at each index is the product of all the elements in the original array except for the element at that index.

#For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].

#You cannot use division in this problem.

#Here's a start:
def products(nums):
  i = 0
  total = 1
  temparray = []
  k = 0
  while i < len(nums):
    k = 0
    total = 1
    j = i + 1
    if(j == len(nums)):
      j = 0
    while k < len(nums) - 1:
      total *= nums[j]
      j += 1
      k += 1
      if(j == len(nums)):
        j = 0
    temparray.append(total)
    i += 1
  return temparray



  # Fill this in.

print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]
