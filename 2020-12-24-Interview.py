#Hi, here's your problem today. This problem was recently asked by Uber:

#You have a landscape, in which puddles can form. You are given an array of non-negative integers representing the elevation at each location. Return the amount of water that would accumulate if it rains.

#For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.
#       X               
#   X███XX█X              
# X█XX█XXXXXX                   
# [0,1,0,2,1,0,1,3,2,1,2,1]
#Here's your starting pont:
def capacity(arr):
  #is filled if left and right are higher
  #if left is higher, but right isnt go right until you hit one that is higher
  #if the height is lower add 2 instead of one
  total = 0
  i = 1
  j = 0
  subtotal = 0
  while i < len(arr):
    if(i != len(arr) - 1):
      if(arr[i-1] > arr[i] and arr[i+1] > arr[i]):
        total += (arr[i-1] - arr[i])
      elif(arr[i-1] > arr[i] and arr[i+1] <= arr[i]):
        j = i
        while(j < len(arr)):
          if(arr[j+1] > arr[j]):
            subtotal += j - i
            break
          j += 1
        total += subtotal
    i += 1
  return total


print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6
