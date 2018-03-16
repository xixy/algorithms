# coding:utf-8

def find_maximum_subarray_cross_mid(A,low,high,mid):
    '''
    发现跨越中点的最大
    '''
    # 计算左边
    left_sum = -100000
    all_sum = 0
    i = mid
    left_index = mid
    while i >= low:
        all_sum = all_sum + A[i]
        if all_sum > left_sum:
            left_sum = all_sum
            left_index = i
        i = i-1
    # 计算右边
    right_sum = -100000
    all_sum = 0
    i = mid + 1
    right_index = mid
    while i <= high:
        all_sum = all_sum + A[i]
        if all_sum > right_sum:
            right_sum = all_sum
            right_index = i 
        i = i+1           
    return left_index,right_index,right_sum+left_sum

def find_maximum_subarray(A,low,high):
    '''
    递归求取最大子数组
    '''
    if low == high:
        return low, high, A[low]
    mid = (low+high)/2
    cross_left,cross_right,cross_sum = find_maximum_subarray_cross_mid(A, low, high, mid)
    low_left,low_right,low_sum = find_maximum_subarray(A, low, mid)
    high_left, high_right, high_sum = find_maximum_subarray(A, mid+1, high)

    if cross_sum > low_sum and cross_sum > high_sum:
        return cross_left,cross_right,cross_sum
    elif low_sum > cross_sum and low_sum > high_sum:
        return low_left,low_right,low_sum
    else:
        return high_left, high_right, high_sum

if __name__ == "__main__":
    A = [1,2,-3,4,5,-6,7]
    print find_maximum_subarray(A,0,6)
