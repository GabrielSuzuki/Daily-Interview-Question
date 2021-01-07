#Hi, here's your problem today. This problem was recently asked by LinkedIn:

#Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks), count the number of islands present in the grid. The definition of an island is as follows:
#1.) Must be surrounded by water blocks.
#2.) Consists of land blocks (1's) connected to adjacent land blocks (either vertically or horizontally). 
#Assume all edges outside of the grid are water.

#Example: 
#Input: 
#10001
#11000
#10110
#00000

#Output: 3
#Here's your starting point:
class Solution(object):
  def inRange(self, grid, r, c):
    numRow, numCol = len(grid), len(grid[0])
    if r < 0 or c < 0 or r >= numRow or c >= numCol:
      return False
    return True

  def numIslands(self, grid):
    #check if the number is 1
    #check if it is in the first or last row
    #check if the left or right are 1
    #check if the top or bottom are 1
    temp = 0
    temp2 = 0
    side2 = False
    count = 0
    i = 0
    k = 0
    while i < len(grid):
      temp = grid[i]
      while k < len(temp):
        if(temp[k] == 1):
          if(k-1 < 0):
            count += 1
          elif(temp[k-1] == 0):
            count += 1
          if(i > 0):
            temp2 = grid[i-1]
            side2 = True
          if(side2 == True):
            if(temp2[k] == 1):
              count -= 1
            side2 = False
        k +=1
      i += 1
      return count
      
    # Fill this in.

grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]
print(Solution().numIslands(grid))
