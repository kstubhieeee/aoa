def QuickSort(arr,p,r):
  if p<r:
    q=Partition(arr,p,r)
    QuickSort(arr,p,q-1)
    QuickSort(arr,q+1,r)

def Partition(arr,p,r):
  x=arr[r]
  i=p-1
  for j in range(p,r):
    if arr[j]<=x:
      i=i+1
      arr[i],arr[j]=arr[j],arr[i]
  arr[i+1],arr[r]=arr[r],arr[i+1]
  return i+1



arr = []
n = int(input("Enter the number of values: "))
print("Enter the values: ")
for i in range(0, n):
    arr.append(int(input()))  

p = 0
r = len(arr) - 1
QuickSort(arr, p, r)
print("Sorted array:", arr)