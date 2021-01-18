#Hi, here's your problem today. This problem was recently asked by Apple:

#You are given a binary tree representation of an arithmetic expression. In this tree, each leaf is an integer value,, and a non-leaf node is one of the four operations: '+', '-', '*', or '/'.

#Write a function that takes this tree and evaluates the expression.

#Example:
#    *
#   / \
#  +    +
# / \  / \
#3  2  4  5

#This is a representation of the expression (3 + 2) * (4 + 5), and should return 45.

#Here's a starting point:
class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root):
  left = isinstance(root.left.val, int)
  right = isinstance(root.right.val, int)
  leftVal = 0
  rightVal = 0
  total = 0
  if(left and right):
    leftVal = root.left.val
    rightVal = root.right.val
    if(root.val == PLUS):
      total = leftVal + rightVal 
    elif(root.val == MINUS):
      total = leftVal - rightVal
    elif(root.val == TIMES):
      total = leftVal * rightVal
    elif(root.val == DIVIDE):
      total = leftVal /rightVal
  else:
    leftVal = evaluate(root.left)
    rightVal = evaluate(root.right)
    if(root.val == PLUS):
      total = leftVal + rightVal 
    elif(root.val == MINUS):
      total = leftVal - rightVal
    elif(root.val == TIMES):
      total = leftVal * rightVal
    elif(root.val == DIVIDE):
      total = leftVal /rightVal
  return total

  # Fill this in.

tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)
print(evaluate(tree))
# 45
