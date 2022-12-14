from countswaps import CountSwaps

def sort(A:CountSwaps)-> CountSwaps:
    for i in range (1, len(A)):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A.swap((j-1), j)
            j = j-1
    return A
