#coding=utf-8

def quick_sort(A,p,r):
    """
    A: list
    p: int
    r: int
    rtype: list sorted in-place
    """
    if p < r:
        mid = partition(A, p ,r)
        quick_sort(A,p,mid-1)
        quick_sort(A,mid,r)

def partition(A, p, r):
    """
    find the partition index
    """
    x = A[r]
    i = p - 1
    j = p
    while j <= r - 1:
        if A[j] < x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
        j = j + 1
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

if __name__ == "__main__":
    A=[1,4,3,6,2]
    quick_sort(A,0,len(A)-1)
    print A