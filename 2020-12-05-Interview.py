#Hi, here's your problem today. This problem was recently asked by Amazon:

#You are given a 2D array of characters, and a target string. Return whether or not the word target word exists in the matrix. Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.

#Example:
#[['F', 'A', 'C', 'I'],
# ['O', 'B', 'Q', 'P'],
# ['A', 'N', 'O', 'B'],
 #['M', 'A', 'S', 'S']]

#Given this matrix, and the target word FOAM, you should return true, as it can be found going up-to-down in the first column.

#Here's the function signature:
def word_search(matrix, word):
  string tempword 
  
  for i in matrix:
    for j in i:
      
      tempword += i[j]
      if(tempword == word):
        return True
      while k < len(i):
        
        tempword2 += matrix[i[j]]
        i += 1
        if(tempword2 == word):
          return True
      tempword2 = ''
  return False
    
  
matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print(word_search(matrix, 'FOAM'))
# True
