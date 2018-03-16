#coding=utf-8

def left(i):
    return 2 * (i + 1) - 1

def right(i):
    return 2 * (i + 1)

def parent():
    return (i + 1) * 2 - 1

def max_heapify(A, i):
    """
    保持堆的属性
    A: list of ints
    i: index of node to examine

    """
    l = left(i)
    r = right(i)

    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < len(A) and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        max_heapify(A,largest)

def build_max_head(A):
    i = len(A) / 2 - 1
    while i >= 0:
        max_heapify(A, i)
        i -= 1

def head_sort(A):
    result = []
    build_max_head(A)
    while len(A) > 1:
        result.append(A[0])
        A[0],A[len(A)-1] = A[len(A)-1],A[0]
        A = A[:-1]
        max_heapify(A,0)
    result.extend(A)
    return result


if __name__ == '__main__':
    A=[1,2,3,4,5]
    print A
    max_heapify(A,0)
    print A

    A=[1,2,3,4,5]
    build_max_head(A)
    print A

    A=[1,2,3,4,5,7,8,10,400]
    result = head_sort(A)
    print result

