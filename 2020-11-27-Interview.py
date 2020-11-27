#Hi, here's your problem today. This problem was recently asked by Apple:

#Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling (larger than or equal to) of k. If either does not exist, 
# then print them as None.

#Here is the definition of a node for the tree.
class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
  # Fill this in.
  if root_node == None:
    #if there are no items in the tree return None
    return (None,None)
  if root_node.value == k:
    #if the root = k return the root as the ceiling/floor
    return (root_node.value, root_node.value)
  if root_node.value < k:
    if root_node.right.value > k: 
      #ceiling = root
      #floor = right
      return (root_node.right.value, root_node.value)
    else:
      if(root_node.right == None):
        #ceiling = root_node
        #floor = None
        return (None, root_node.value)
      else:
        #Go to the right branch
        findCeilingFloor(root_node.right, k)
  elif root_node.value > k:
    if root_node.left.value < k:
      #ceiling = root
      #floor = left
      return (root_node.left.value, root_node.value)
    else:
      if(root_node.left == None):
        #ceiling = root_node
        #floor = None
        return (None, root_node.value)
      else:
        #Go to the left branch
        findCeilingFloor(root_node.left, k)


root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print(findCeilingFloor(root, 5))
# (4, 6)
