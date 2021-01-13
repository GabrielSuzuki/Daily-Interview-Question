#Hi, here's your problem today. This problem was recently asked by Facebook:

#Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.

#Example:
#Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
#Output: ['0->2', '5->5', '7->11', '15->15']
#Assume that all numbers will be greater than or equal to 0, and each element can repeat.

#Here is a starting point:
def findRanges(nums):
  i = 0
  firstbool = True
  firstint = 0
  firststring = ""
  secondint = 0
  secondstring = ""
  tempphrase = ""
  finalarray = []
  while i < len(nums):
    if(firstbool == True):
      firstbool = False
      firstint = nums[i]
    if(i + 1 < len(nums)):
      if(nums[i + 1] - nums[i] > 1 ):
        secondint = nums[i]
        firstbool = True
        firststring = str(firstint)
        secondstring = str(secondint)
        tempphrase = firststring + "->" + secondstring
        finalarray.append(tempphrase)
    else:
      secondint = firstint
      firststring = str(firstint)
      secondstring = str(secondint)
      tempphrase = firststring + "->" + secondstring
      finalarray.append(tempphrase)
    i += 1
  return finalarray
  # Fill this in.

print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']
