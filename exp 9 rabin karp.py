def rabin_karp(text, pattern):
  prime = 101
  n = len(text)
  m = len(pattern)
  prime_power = pow(prime, m - 1)
  pattern_hash = 0
  window_hash = 0
  for i in range(m):
      pattern_hash = (pattern_hash * prime + ord(pattern[i])) % prime
      window_hash = (window_hash * prime + ord(text[i])) % prime

  matches = []

  for i in range(n - m + 1):
      if pattern_hash == window_hash:
          match = True
          for j in range(m):
              if text[i + j] != pattern[j]:
                  match = False
                  break
          if match:
              matches.append(i)

      if i < n - m:
          window_hash = (window_hash - ord(text[i]) * prime_power) % prime
          window_hash = (window_hash * prime + ord(text[i + m])) % prime
          window_hash = (window_hash + prime) % prime

  return matches

text = "abracadabra"
pattern = "abra"
print("Pattern found at positions:", rabin_karp(text, pattern))
