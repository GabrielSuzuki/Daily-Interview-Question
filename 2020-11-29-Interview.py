class MaxStack:
  def __init__(self):
    self.head = None
    # Fill this in.

  def push(self, val):
    if not self.head:
      self.head = val
      return
    for current_node in self:
      pass
    current_node.next = val
    # Fill this in.

  def pop(self):
    if not self.head:
      return
    for current_node in self:
      pass
    current_node = None

  def max(self):
    saved_node = 0
    if not self.head:
      return 
    for current_node in self:
      if current_node > saved_node:
        saved_node = current_node
    return saved_node

    
    # Fill this in.

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2

