#Hi, here's your problem today. This problem was recently asked by LinkedIn:

#Write a function that reverses the digits a 32-bit signed integer, x. Assume that the environment can only store integers within the 32-bit signed integer range, 
#[-2^31, 2^31 - 1]. The function returns 0 when the reversed integer overflows. 

#Example:
#Input: 123
#Output: 321
class Solution:
  def reverse(self, x):
    a = 0
    rev = 0  
    while(x > 0): 
      a = x % 10
      rev = rev * 10 + a 
      x = x / 10      
    return rev 

print(Solution().reverse(123))
# 321
print(Solution().reverse(2**31))
# 0
