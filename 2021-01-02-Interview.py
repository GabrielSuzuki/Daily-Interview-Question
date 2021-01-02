#Hi, here's your problem today. This problem was recently asked by Microsoft:

#You are given the preorder and inorder traversals of a binary tree in the form of arrays. Write a function that reconstructs the tree represented by these traversals.

#Example:
#Preorder: [a, b, d, e, c, f, g]
#Inorder: [d, b, e, a, f, c, g]

#The tree that should be constructed from these traversals is:
#    a
#   / \
#  b   c
# / \ / \
#d  e f  g

#Here's a start:
from collections import deque

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __str__(self):
    q = deque()
    q.append(self)
    result = ''
    while len(q):
      n = q.popleft()
      result += n.val
      if n.left:
        q.append(n.left)
      if n.right:
        q.append(n.right)

    return result


def reconstruct(preorder, inorder):
  inStrt = 0
  inEnd = len(inorder)-1
  if (inStrt > inEnd):
        return None
 
    # Pich current node from Preorder traversal using
    # preIndex and increment preIndex
  tNode = Node(preorder[reconstruct.preIndex])
  reconstruct.preIndex += 1
 
    # If this node has no children then return
  if inStrt == inEnd :
      return tNode
 
    # Else find the index of this node in Inorder traversal
  inIndex = search(inorder, inStrt, inEnd, tNode.data)
     
    # Using index in Inorder Traversal, construct left 
    # and right subtrees
  tNode.left = reconstruct(inorder, preorder, inStrt, inIndex-1)
  tNode.right = reconstruct(inorder, preorder, inIndex + 1, inEnd)
 
  return tNode

tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                   ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
print(tree) 
