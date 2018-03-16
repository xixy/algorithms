#coding=utf-8

class node(object):
    """用来表示bucket中的链表的节点"""
    def __init__(self, val):
        self.val = val
        self.next = None

def bucket_sort(A):
    """
    桶排序
    A:list [0,1.0.4,0.56,0.2]
    """
    buckets = [None]*10
    for item in A:
        index = int(item)
        if buckets[index] == None:
            buckets[index] = node(item)
        #如果不为零，则需要插入链表，这个过程中顺便排序吧
        else:
            p = buckets[index]
            pre = p
            while p != None and p.val < item:
                pre = p
                p = p.next
            #插入链表尾部
            if p == None:
                pre.next = node(item)
            #插入链表第一位
            elif pre == p:
                buckets[index] = node(item)
                buckets[index].next = p
            else:
                #插入链表中间
                temp = node(item)
                pre.next = temp
                temp.next = p

    #输出
    result = []
    for head in buckets:
        while head != None:
            result.append(head.val)
            head = head.next

    return result

if __name__ == '__main__':
    A=[0.1,0.34,0.24,0.61,0.15,0.92,0.151,0.108,0.129]
    print bucket_sort(A)




