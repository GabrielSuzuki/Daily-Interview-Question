#Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
#Input: [3, 3, 2, 1, 3, 2, 1]
#Output: [1, 1, 2, 2, 3, 3, 3]

def sortNums(nums):
  i = 0
  j = 0
  # Fill this in.
  sortedlist = []
  for k in nums:
    if nums[k] == 1:
      #place at beginning 
      sortedlist.insert(0,nums[k])
      i += 1
    elif nums[k] == 2:
      #place at i position
      sortedlist.insert(i,nums[k])
      j += 1
    elif nums[k] == 3:
      #place at end
      sortedlist.insert((j+i),nums[k])
  return sortedlist
print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]

#Challenge: Try sorting the list using constant space.
