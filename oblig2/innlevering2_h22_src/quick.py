from countswaps import CountSwaps

def sort(A: CountSwaps)-> CountSwaps:
    return QuickSort(A, 0, len(A)-1)
   
def Partition(A: CountSwaps, low, high):
    pivot = A[high]
    left = low
    right = high-1

    while left <= right:
        while left <= right and A[left] < pivot:
            left += 1
        while right >= left and A[right] >= pivot:
            right -= 1
        if left < right:
            A.swap(left, right)
    A.swap(left, high)
    return left


def QuickSort(A: CountSwaps, low, high) -> CountSwaps:
    if low >= high: return A
    p = Partition(A, low, high)
    QuickSort(A, low, p-1)
    QuickSort(A, p+1, high)
    return A
