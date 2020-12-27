#Hi, here's your problem today. This problem was recently asked by Google:

#You are given the root of a binary tree. Return the deepest node (the furthest node from the root).

#Example:
#    a
#   / \
#  b   c
# /
#d

#The deepest node in this tree is d at depth 3.

#Here's a starting point:
class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __repr__(self):
    # string representation
    return self.val


def deepest(node):
  #Use a recursive statement to check both sides if they are empty nodes or not
  #needs to return both the depth and letter at that depth
  # Fill this in.
  #testNode = node
  deepestnode = "x"
  depth = 0
  maxdepth = 0
  temparr = [deepestnode,maxdepth]
  if(node == None):
    return 
  if(node.left != None):
    temparr = deepest(node.left)
    depth = temparr[1] + 1
  maxdepth = depth
  depth = 0
  if(node.right != None):
    temparr = deepest(node.right)
    depth = temparr[1] + 1
  if(maxdepth < depth):
    maxdepth = depth
  if(node.right == None and node.left == None):
    maxdepth += 1 

    temparr = [node.val,maxdepth]
    return temparr
  return temparr


root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root))
# (d, 3)
