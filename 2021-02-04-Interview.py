#Hi, here's your problem today. This problem was recently asked by LinkedIn:

#Given a string, rearrange the string so that no character next to each other are the same. If no such arrangement is possible, then return None.

#E3xample:
#Input: abbccc
#Output: cbcbca
def rearrangeString(s):
  #temp = ''
  endingstring = ""
  tempstring = ""
  i = 0
  while i < len(s):
    if(i > 0):
      if(s[i] == s[i-1]):
        if(i+1 < len(s)):
          endingstring += s[i+1]
          endingstring += s[i]
          i += 1
        else:
          #tempstring = endingstring
          endingstring = s[i] + endingstring
          return endingstring
        k= i + 1
        tempstring = endingstring
        while(k < len(s)):
          tempstring += s[k]
          k +=1 
        s = tempstring
      elif(i < len(s)):
        endingstring += s[i]
    else:
      endingstring += s[i]
    i += 1
  return endingstring
  # Fill this in.

print(rearrangeString('abbccc'))
# cbcabc
