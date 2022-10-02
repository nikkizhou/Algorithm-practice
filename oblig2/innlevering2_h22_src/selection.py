from countswaps import CountSwaps

def sort(A:CountSwaps)-> CountSwaps:
  for i in range(0,len(A)):
    k=i
    for j in range(i+1,len(A)):
      if A[j]<A[k]:
        k=j
    if i!=k:
      A.swap(i,k)
  return A
