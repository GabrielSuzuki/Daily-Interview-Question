#Hi, here's your problem today. This problem was recently asked by AirBNB:

#Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

#Example 1:
#Input: A = "ab", B = "ba"
#Output: true
#Example 2:

#Input: A = "ab", B = "ab"
#Output: false
#Example 3:
#Input: A = "aa", B = "aa"
#Output: true
#Example 4:
#Input: A = "aaaaaaabc", B = "aaaaaaacb"
#Output: true
#Example 5:
#Input: A = "", B = "aa"
#Output: false
#Here's a starting point:
class Solution:
  def buddyStrings(self, A, B):
    # loop through each at the same time \
    #check each spot to see if they are different
    # if there are more than 2 differences then say false
    # difference 1 of A = difference 2 of B and difference 1 of B = difference 2 of A, then true
    # else false
    i = 0
    differences = 0
    #diff1A = ""
    #diff1B = ""
    #diff2A = ""
    #diff2B = ""
    #first = True
  
    if(len(A) != len(B)):
      return False
    while i < len(A):
      if(A[i] != B[i]):
        differences += 1
        #if(first == True):
         # first == False
          #diff1A = A[i]
          #diff1B = B[i]
        #else:
         # diff2A = A[i]
          #diff2B = B[i]
      i += 1
    if(differences > 2):
      return False
    elif(differences == 2):
     # if(diff1A == diff2B and diff1B == diff2A):
      return True
      #else:
       # return False
    else:
      return True





print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False
