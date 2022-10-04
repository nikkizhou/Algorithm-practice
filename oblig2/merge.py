from countswaps import CountSwaps

def sort(A:CountSwaps)->CountSwaps:
  if len(A)<=1: return A
  i=round(len(A)/2)
  A1= sort(A[:i])
  A2= sort(A[i:])
  return merge(A1,A2,A)


def merge(A1,A2,A):
  i=0
  j=0
  while i<len(A1) and j <len(A2):
    if A1[i]<=A2[j]:
      A[i+j]=A1[i]
      i+=1
    else:
      A[i+j]=A2[j]
      j+=1

  while i<len(A1):
    A[i+j]=A1[i]
    i+=1

  while j<len(A2):
    A[i+j]=A2[j]
    j+=1

  return A
