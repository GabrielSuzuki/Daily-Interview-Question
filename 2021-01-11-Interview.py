#Hi, here's your problem today. This problem was recently asked by Google:

#You are given an array of tuples (start, end) representing time intervals for lectures. The intervals may be overlapping. Return the number of rooms that are required.

#For example. [(30, 75), (0, 50), (60, 150)] should return 2.
def time_intervals(intervals):
  beginning1 = 0
  end1 = 0
  beginning2 = 0
  end2 = 0
  i = 0
  j = 0
  count = 0
  for k in intervals:
    while i < len(k):
      beginning1 = k[0]
      end1 = k[1]
      if(i + 1 < len(k)):
        j = i + 1
        while j < len(k):
          beginning2 = k[0] 
          end2 = k[1]
          if(beginning1 > beginning2 and beginning1 < end2):
            count -= 1
          j += 1
      i += 1
    count += 1
    return count


print(time_intervals([(30, 75), (0, 50), (60, 150)]))