def SelectionSort(arr, n):
  for i in range(0, n - 1):
    min = i
    for j in range(i + 1, n):
      if arr[min] > arr[j]:
        min = j
    if min != i:
      arr[i], arr[min] = arr[min], arr[i]


list = [7, 4, 2, 6, 5, 1]
n = len(list)
SelectionSort(list, n)
print(list)
