
#Hi, here's your problem today. This problem was recently asked by Google:

#You are given a stream of numbers. Compute the median for each new element .

#Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]

#Here's a starting point:
def running_median(stream):
  i = 0
  unsortedlist = []
  sortedlist = []
  finallist = []
  tempvalue = 0
  tempvalue2 = 0
  evenvalue = 0
  while i < len(stream):
    unsortedlist.append(stream[i])
    sortedlist = sorted(unsortedlist)
    if len(sortedlist) == 1:
      finallist.append(sortedlist[i])
    elif len(sortedlist) % 2 != 0:
      #odd
      tempvalue = int(len(sortedlist)/2 - 0.5)
      finallist.append(sortedlist[tempvalue])
    elif len(sortedlist) % 2 == 0:
      #even
      tempvalue = int(len(sortedlist)/2 - 1)
      tempvalue2 = int(len(sortedlist)/2)
      evenvalue = (sortedlist[tempvalue] + sortedlist[tempvalue2])/2
      finallist.append(evenvalue)
    i += 1
  return finallist
  # Fill this in.

print(running_median([2, 1, 4, 7, 2, 0, 5]))
# 2 1.5 2 3.0 2 2.0 2
