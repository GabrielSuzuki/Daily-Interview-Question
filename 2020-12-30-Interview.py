#Hi, here's your problem today. This problem was recently asked by Amazon:

#Given a binary tree, return all values given a certain height h.

#Here's a starting point:
class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def valuesAtHeight(root, height):
  #check if the left and right are None
  #if so
  values = [] 
  if(root == None):
    return values
  if(height == 1):
    values.append(root.value)
  height -= 1 
  if(root.left != None):
    left = (valuesAtHeight(root.left,height))
    for i in left:
      values.append(i)
  if(root.right != None):
    right = (valuesAtHeight(root.right,height))
    for j in right:
      values.append(j)
  return values

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(valuesAtHeight(a, 3))
# [4, 5, 7]

