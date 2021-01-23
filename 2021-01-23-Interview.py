#Hi, here's your problem today. This problem was recently asked by Uber:

#Design a simple stack that supports push, pop, top, and retrieving the minimum element in constant time.

#push(x) -- Push element x onto stack.
#pop() -- Removes the element on top of the stack.
#top() -- Get the top element.
#getMin() -- Retrieve the minimum element in the stack.

#Note: be sure that pop() and top() handle being called on an empty stack.
class Node: 
    # Constructor which assign argument to nade's value  
    def __init__(self, value): 
        self.value = value 
        self.next = None
  
    # This method returns the string representation of the object. 
    def __str__(self): 
        return "Node({})".format(self.value) 
      
    # __repr__ is same as __str__ 
    __repr__ = __str__ 
  
class minStack(object):
  def __init__(self):
    self.top = None
    self.count = 0
    self.minimum = None
    # Fill this in.

  def push(self, value):
    if self.top is None: 
      self.top = Node(value) 
      self.minimum = value 
          
    elif value < self.minimum: 
        temp = (2 * value) - self.minimum 
        new_node = Node(temp) 
        new_node.next = self.top 
        self.top = new_node 
        self.minimum = value 
    else: 
        new_node = Node(value) 
        new_node.next = self.top 
        self.top = new_node 
    # Fill this in.

  def pop(self):
    if self.top == None:
      return "stack is empty"
    else: 
      removedNode = self.top.value 
      self.top = self.top.next
      if removedNode < self.minimum: 
        self.minimum = ( ( 2 * self.minimum ) - removedNode )
        return self.minimum 
      else: 
        return removedNode
    # Fill this in.

  def topf(self):
    if self.top == None:
      return "stack is empty"
    else:
      if self.top.value < self.minimum:
        return self.minimum
      else:
        return self.top.value
    # Fill this in.

  def getMin(self):
    if self.top is None:
      return "stack is empty"
    else:
      return self.minimum
    # Fill this in.

x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
# -3
x.pop()
print(x.topf())
# 0
print(x.getMin())
# -2
