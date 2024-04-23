def InsertionSort(arr):
  for i in range(1, len(arr)):
    temp = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > temp:
      arr[j + 1] = arr[j]
      j = j - 1
    arr[j + 1] = temp


list = [2, 9, 1, 5, 7, 4, 8]
InsertionSort(list)
print(list)
