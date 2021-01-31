#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

#Given a number n, print the n-th Fibonacci Number. 
#Examples:
#Input: n = 3
#Output: 2

#Input: n = 7
#Output: 13
#Here's a starting point:
def fibonacci(n):
    first = 0
    second = 1
    iterator = 2
    if n >= 2:
      while iterator < n + 1:
        third = second + first
        first = second
        second = third
        iterator += 1
      return third
    elif n == 1:
      return 1
    else:
      return 0
    # fill this in.

n = 9
print(fibonacci(n))
# 34
