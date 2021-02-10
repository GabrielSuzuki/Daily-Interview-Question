#Hi, here's your problem today. This problem was recently asked by Amazon:

#You are given an array of integers, and an integer K. Return the subarray which sums to K. You can assume that a solution will always exist.
def find_continuous_k(list, k):
  n_sum = 0
  s = set()
  temparray = []

  for i in range(k):
    n_sum += list[i]
    temparray.append(list[i])
    if n_sum == 0 or n_sum in s:
      return temparray
    s.add(n_sum)
  return 0

print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))
# [2, 5, 7]
