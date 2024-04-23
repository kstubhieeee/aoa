def MinMax(arr, i, j):
  if i == j:
      return arr[i], arr[i]

  mid = (i + j) // 2

  min1, max1 = MinMax(arr, i, mid)
  min2, max2 = MinMax(arr, mid + 1, j)

  overall_min = min(min1, min2)
  overall_max = max(max1, max2)

  return overall_min, overall_max


arr_input = list(map(int, input("Enter elements of the array: ").split()))


min_val, max_val = MinMax(arr_input, 0, len(arr_input) - 1)


print("Minimum value:", min_val)
print("Maximum value:", max_val)
