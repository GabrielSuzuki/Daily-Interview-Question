#Hi, here's your problem today. This problem was recently asked by Microsoft:

#A k-ary tree is a tree with k-children, and a tree is symmetrical if the data of the left side of the tree is the same as the right side of the tree. 

#Here's an example of a symmetrical k-ary tree.
#        4
#     /     \
#    3        3
#  / | \    / | \
#9   4  1  1  4  9
#Given a k-ary tree, figure out if the tree is symmetrical. 

#Here is a starting point:
class Node():
  def __init__(self, value, children=[]):
    self.value = value
    self.children = children

def is_symmetric(root1,root2):
  # If both trees are empty, then they are mirror images
    if root1 is None and root2 is None:
      return True
 
    #""" For two trees to be mirror images, 
    #    the following three conditions must be true
    #    1 - Their root node's key must be same
    #    2 - left subtree of left tree and right subtree
    #      of the right tree have to be mirror images
    #    3 - right subtree of left tree and left subtree
    #       of right tree have to be mirror images
    #"""

    if (root1 is not None and root2 is not None):
      if root1.value == root2.value:
        i = 0
        k = 0
        k = len(root2.children) - 1
        while i < len(root1.children):
         # print(root1.children[i].value)
         # print(root2.children[k].value)
          if(root1.children[i].value != root2.children[k].value):
            return False
         # print(k)
         # print(i)
          k -= 1
          i += 1
         # print(k)
         # print(i)
        return True

 

  # Fill this in.

tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
root1 = tree.children[0]
tree.children[1].children = [Node(1), Node(4), Node(9)]
root2 = tree.children[1]
print(is_symmetric(root1,root2))
# True
