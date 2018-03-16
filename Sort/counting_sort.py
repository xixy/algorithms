#coding=utf-8


def counting_sort(A):
    """
    计数排序
    """
    i = k = max(A) 
    C = []
    while i >= 0:
        C.append(0)
        i -= 1
    for item in A:
        C[item] += 1

    i = 1
    while i <= k:
        C[i] += C[i-1] #C[i]表示小于或等于i的元素个数
        i += 1

    B = [0]*(len(A)+1)
    i = len(A) - 1
    while i >= 0:
        B[C[A[i]]] = A[i]
        C[A[i]] -= 1
        i -= 1
    return B[1:]



if __name__ == '__main__':
    A=[5,4,1,6,10,0]
    print counting_sort(A)