#Hi, here's your problem today. This problem was recently asked by Microsoft:

#You are given a doubly linked list. Determine if it is a palindrome. 

#Can you do this for a singly linked list?
class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None

def is_palindrome(node):
  i = 0
  count = 0
  temparray = []
  tempnode = node 
  while tempnode != None:
    tempnode = tempnode.next
    count += 1
  if(count % 2 == 0):#even
    while i < count / 2:
      temparray.append(node.val)
      node = node.next
      i += 1
    j = i
    i = 0
    while i < count / 2:
      if(temparray[j - 1] != node.val):
        return False
      node = node.next
      j -= 1
      i += 1

  else:#odd
    while i < count / 2:
      temparray.append(node.val)
      node = node.next
      i += 1
    j = i
    i = 0
    node = node.next
    while i < count / 2:
      if(temparray[j - 1] != node.val):
        return False
      node = node.next
      j -= 1
      i += 1
  return True
  # Fill this in.

node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next

print(is_palindrome(node))
# True
