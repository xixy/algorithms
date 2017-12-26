# coding: utf-8

def find_insert_point(sorted_list,x):
    '''
    需要插入到begin的前面
    '''
    begin = 0
    end = len(sorted_list) - 1
    while begin <= end:
        middle = (begin + end) / 2
        if (sorted_list[middle] > x):
            end = middle - 1
        else:
            begin = middle + 1
    return begin



def binary_insertion_sort(unsorted):
    '''
    返回插入排序结果
    Args:
        unsorted:未排序的list
    Return：
        排序的list

    '''
    if len(unsorted) <= 1:
        return unsorted

    size = len(unsorted)
    i = 1
    while i <= size - 1:
        temp = unsorted[i]
        #对第j个元素进行排序
        x = find_insert_point(unsorted[:i],unsorted[i])
        # 往后排
        j = i
        while j > x:
            unsorted[j] = unsorted[j-1]
            j = j - 1
        unsorted[x] = temp
        i = i + 1

    return unsorted   


def straight_insertion_sort(unsorted):
    '''
    返回插入排序结果
    Args:
        unsorted:未排序的list
    Return：
        排序的list

    '''
    if len(unsorted) <= 1:
        return unsorted

    size = len(unsorted)
    i = 1
    while i <= size - 1:
        j = i
        while j > 0:
            if unsorted[j] < unsorted[j-1]:
                temp = unsorted[j-1]
                unsorted[j-1] = unsorted[j]
                unsorted[j] = temp
                j = j-1
            else:
                break
        i = i + 1
    return unsorted



if __name__ == '__main__':
    a = [1,4,3,2,-10,4,56]
    print binary_insertion_sort(a)
