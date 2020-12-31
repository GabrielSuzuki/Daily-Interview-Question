#Hi, here's your problem today. This problem was recently asked by Amazon:

#You are given a string s, and an integer k. Return the length of the longest substring in s that contains at most k distinct characters.

#For instance, given the string:
#aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff. The answer should be 5.

#Here's a starting point:
def longest_substring_with_k_distinct_characters(s, k):
  step = 0
  strarr = [""]
  i = 0
  j = 0
  maximum = 0
  while i < len(s):
    hit = False
    if step > k:
      maximum = len(strarr)
      step = 0
      strarr = [""]
    for j in strarr:
      if j == s[i]:
        strarr.append(j)
        hit = True
        break
    if hit == False:
      if(step < k):
        strarr.append(s[i])
      step += 1
    i += 1
  return maximum# Fill this in.

print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)

