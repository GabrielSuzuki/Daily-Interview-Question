#Hi, here's your problem today. This problem was recently asked by Microsoft:

#You are given an array of integers. Return the length of the longest increasing subsequence (not necessarily contiguous) in the array. 

#Example:
#[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

#The following input should return 6 since the longest increasing subsequence is 0, 2, 6, 9 , 11, 15.
global maximum 
  
def _lis(arr , n ): 
  
    # to allow the access of global variable 
    global maximum 
  
    # Base Case 
    if n == 1 : 
        return 1
  
    # maxEndingHere is the length of LIS ending with arr[n-1] 
    maxEndingHere = 1
  
    for i in range(1, n): 
        res = _lis(arr , i) 
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere: 
            maxEndingHere = res +1
  
    # Compare maxEndingHere with overall maximum. And 
    # update the overall maximum if needed 
    if(maximum < maxEndingHere):
      maximum = maxEndingHere
  
    return maxEndingHere 
  
def lis(arr): 
  
    # to allow the access of global variable 
    global maximum 
  
    # lenght of arr 
    n = len(arr) 
  
    # maximum variable holds the result 
    maximum = 1
  
    # The function _lis() stores its result in maximum 
    _lis(arr , n) 
  
    return maximum 
  
# Driver program to test the above function 
arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
n = len(arr) 
print(lis(arr)) 
