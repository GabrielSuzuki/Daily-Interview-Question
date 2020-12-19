#Hi, here's your problem today. This problem was recently asked by Apple:

#You are given an array. Each element represents the price of a stock on that particular day. Calculate and return the maximum profit you can make from buying and selling that stock only once.

#For example: [9, 11, 8, 5, 7, 10]

#Here, the optimal trade is to buy when the price is 5, and sell when it is 10, so the return value should be 5 (profit = 10 - 5 = 5).

#Here's your starting point:
def buy_and_sell(arr):
  savednum1 = arr[0]
  savedpos1 = 0
  savednum2 = arr[0]
  i = 0
  k = 0 
  j = 0
  for i in arr:
    if arr[j] < savednum1:
      savednum1 = i
      savedpos1 = j
    j += 1
  j = 0
  for k in arr:
    if savedpos1 < j:
      if arr[j] > savednum2:
        savednum2 = k
    j += 1
  return savednum2 - savednum1

  #Fill this in.
  
print(buy_and_sell([9, 11, 8, 5, 7, 10]))
# 5
