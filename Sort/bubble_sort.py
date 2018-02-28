# coding: utf-8

def bubble_sort(unsorted):
    '''
    冒泡排序

    '''
    i = len(unsorted) - 1
    while i > 0:
        for j in range(0,i):
            if unsorted[j] > unsorted[j+1]:
                temp = unsorted[j]
                unsorted[j] = unsorted[j+1]
                unsorted[j+1] = temp
        i = i - 1
    return unsorted

if __name__ == '__main__':
    a = [1,4,3,2,-10,56,7]
    print bubble_sort(a)