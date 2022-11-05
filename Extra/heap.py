def heapify(arr, n, i):
  smallest = i #Initialize smallest as root
  l,r = 2 * i + 1 , 2 * i + 2 
  if (l < n and arr[l] < arr[smallest]): smallest = l
  if (r < n and arr[r] < arr[smallest]): smallest = r
  # If smallest is not root
  if (smallest != i):
    arr[i],arr[smallest]=arr[smallest],arr[i]
    heapify(arr, n, smallest)
 
def deleteRoot(arr):
  global n
  lastElement = arr[n - 1]
  arr[0] = lastElement
  n = n - 1
  heapify(arr, n, 0)
 

def heapify(arr, n, i):
  parent = int(((i-1)/2))
  if i>0 and arr[i] < arr[parent]:
    arr[i], arr[parent] = arr[parent], arr[i]
    heapify(arr, n, parent)
 
def insertNode(arr, key):
  global n
  n += 1
  arr.append(key)
  heapify(arr, n, n-1)


