#Hi, here's your problem today. This problem was recently asked by Twitter:

#You are given an array of k sorted singly linked lists. Merge the linked lists into a single sorted linked list and return it.

#Here's your starting point:
class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer

def merge(lists):
  #c = Node(None)
  #while lists.next != None:
    #check if the next item is greater than the first item
    #if so repeat to next item
   # if lists.val > c.val:
  for i in range(1, len(lists)):
        while (True):
            # head of both the lists,
            # 0 and ith list.
            head_0 = lists[0]
            head_i = lists[i]
 
            # Break if list ended
            if (head_i == None):
                break
 
            # Smaller than first 
            # element
            if (head_0.val >=
                head_i.val):
                lists[i] = head_i.next
                head_i.next = head_0
                lists[0] = head_i
            else:
                # Traverse the first list
                while (head_0.next != None):
                    # Smaller than next 
                    # element
                    if (head_0.next.val >=
                        head_i.val):
                        lists[i] = head_i.next
                        head_i.next = head_0.next
                        head_0.next = head_i
                        break
                    # go to next node
                    head_0 = head_0.next
                    # if last node
                    if (head_0.next == None):
                        lists[i] = head_i.next
                        head_i.next = None
                        head_0.next = head_i
                        head_0.next.next = None
                        break
  return lists[0]    
 

a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(merge([a, b]))
# 123456

