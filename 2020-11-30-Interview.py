#Hi, here's your problem today. This problem was recently asked by LinkedIn:

#You are given a positive integer N which represents the number of steps in a staircase. You can either climb 1 or 2 steps at a time. Write a function that returns the
# number of unique ways to climb the stairs.
def staircase(n):
  # Fill this in.
  ways = 0
  if(n == 0):
    ways += 1
  if(n-2 >= 0):#2 steps
    ways += staircase(n-2)
  if(n-1 >= 0):#1 step
    ways += staircase(n-1)
  return ways

  
print(staircase(4))
# 5
print(staircase(5))
# 8

#Can you find a solution in O(n) time?
