def naive_string_matching(text, pattern):
  n = len(text)
  m = len(pattern)
  matches = []

  for i in range(n - m + 1):
      j = 0
      while j < m and text[i + j] == pattern[j]:
          j += 1
      if j == m:
          matches.append(i)

  return matches


text = "abracadabra"
pattern = "abra"
print("Pattern found at positions:", naive_string_matching(text, pattern))
