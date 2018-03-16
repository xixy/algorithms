#coding=utf-8

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def print_list(head):
    node = head
    string = ""
    while node != None:
        string = string +" "+ str(node.val)
        node = node.next
    print string

def search(val,head):
    result = []
    p = head
    while p != None:
        if val == p.val:
            result.append(p.val)
        p = p.next
    return result

def insert(val,head):
    dummy = ListNode(0)
    dummy.next = head
    node = ListNode(val)
    p1 = dummy
    p2 = p1.next
    while p2 != None:
        if p2.val >= val:
            p1.next = node
            node.next = p2
            break
        p1,p2 = p2,p2.next
    return dummy.next

def delete(val,head):
    dummy = ListNode(0)
    dummy.next = head
    p1 = dummy
    p2 = head
    while p2 != None:
        if p2.val == val:
            p1.next = p2.next
        p1,p2 = p2,p2.next
    return dummy.next

if __name__ == '__main__':
    a = ListNode(0)
    b = ListNode(10)
    c = ListNode(5)
    a.next = b
    b.next = c
    a = insert(3,a)
    print_list(a)
    a = delete(10,a)
    print_list(a)
