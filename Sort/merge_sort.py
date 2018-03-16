# coding: utf-8



def merge_sort(unsorted):
    '''
    返回归并排序结果
    Args:
        unsorted:未排序的list
    Return：
        排序的list

    '''
    size = len(unsorted)
    if size == 1:
        return unsorted
    middle = size / 2 + size % 2
    a = unsorted[:middle]
    b = unsorted[middle:]

    a = merge_sort(a)
    b = merge_sort(b)

    #进行merge
    result = []
    while a != [] and b != []:
        if a[0] < b[0]:
            result.append(a[0])
            a.pop(0)
        else:
            result.append(b[0])
            b.pop(0)
    result.extend(a)
    result.extend(b)
    return result

if __name__ == '__main__':
    a = [1,4,3,2,-10,4,56,7]
    print merge_sort(a)
