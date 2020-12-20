#Hi, here's your problem today. This problem was recently asked by Apple:

#Implement a queue class using two stacks. A queue is a data structure that supports the FIFO protocol (First in = first out). Your class should support the enqueue and dequeue methods like a standard queue.

#Here's a starting point:


class Queue:
  def __init__(self):
    self.s1 = []
    self.s2 = []
    # Fill this in.
    
  def enqueue(self, val):
    # Move all elements from s1 to s2  
      while len(self.s1) != 0:  
          self.s2.append(self.s1[-1])  
          self.s1.pop() 
  
        # Push item into self.s1  
      self.s1.append(val)  
  
        # Push everything back to s1  
      while len(self.s2) != 0:  
          self.s1.append(self.s2[-1])  
          self.s2.pop() 
    # Fill this in.

  def dequeue(self):
    # if first stack is empty  
      if len(self.s1) == 0:  
          print("Q is Empty") 
      
        # Return top of self.s1  
      x = self.s1[-1]  
      self.s1.pop()  
      return x 
    # Fill this in.

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3
