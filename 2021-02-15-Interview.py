#You are given the root of a binary tree. Find the level for the binary tree with the minimum sum, and return that value.

#For instance, in the example below, the sums of the trees are 10, 2 + 8 = 10, and 4 + 1 + 2 = 7. So, the answer here should be 7.
class Node:
  def __init__(self, value, left=None, right=None):
    self.val = value
    self.left = left
    self.right = right

def minimum_level_sum(root):
  sum1 = 0
  sum2 = 0
  sum1 = root.val
  if(root.left != None):
    sum2 += minimum_level_sum(root.left)
  if(root.right != None):
    sum2 += minimum_level_sum(root.right)
  print(sum2)
  #print(sum1)
  if(sum1 > sum2):
    return sum1
  else:
    return sum2 

  # Fill this in.

#     10
#    /  \
#   2    8
#  / \    \
# 4   1    2
node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)

print(minimum_level_sum(node))

