def longest_common_subsequence(X, Y):
  m = len(X) #len = 7
  n = len(Y) #len = 5

  
  lcs_matrix = [[0] * (n + 1) for _ in range(m + 1)]

  
  for i in range(1, m + 1):
      for j in range(1, n + 1):
          if X[i - 1] == Y[j - 1]:
              lcs_matrix[i][j] = lcs_matrix[i - 1][j - 1] + 1
          else:
              lcs_matrix[i][j] = max(lcs_matrix[i - 1][j], lcs_matrix[i][j - 1])

 
  lcs = []
  i, j = m, n
  while i > 0 and j > 0:
      if X[i - 1] == Y[j - 1]:
          lcs.append(X[i - 1])
          i -= 1
          j -= 1
      elif lcs_matrix[i - 1][j] > lcs_matrix[i][j - 1]:
          i -= 1
      else:
          j -= 1

 
  lcs.reverse()

  return lcs

#main
X = "ABCBDAB"
Y = "BDCAB"
print("Longest Common Subsequence:", ''.join(longest_common_subsequence(X, Y)))