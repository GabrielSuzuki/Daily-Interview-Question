#Hi, here's your problem today. This problem was recently asked by Uber:

#You are given a string of parenthesis. Return the minimum number of parenthesis that would need to be removed in order to make the string valid. "Valid" means that each open parenthesis has a matching closed parenthesis.

#Example:

#"()())()"

#The following input should return 1.

#")("

#Here's a start:
def count_invalid_parenthesis(string):
  #opent = False
  #count = 0
  #for element in range(0, len(string)):  
  #  if string[element] == '(':
  #    opent == True
  #  if string[element] == ')':
  #    if opent == False:
  #      count += 1
  #    opent = False
  #return count
  cnt = 0
  for i in range(len(string)): 
    if (string[i] == '('): 
      cnt += 1
    elif (string[i] == ')'): 
      cnt -= 1
  cnt = abs(cnt)
  return cnt
print(count_invalid_parenthesis("()())()"))
# 1
