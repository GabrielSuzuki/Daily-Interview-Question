#Hi, here's your problem today. This problem was recently asked by Microsoft:

#Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.
def calcAngle(h, m):
  total = 0
  total = 6 * m - (30 * h + m / 2)
  if total < 0:
      total = 360 + total
  return total

print(calcAngle(3, 30))
# 75
print(calcAngle(12, 30))
# 165
