# coding: utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list(head):
    node = head
    string = ""
    while node != None:
        string = string +" "+ str(node.val)
        node = node.next
    print string


class Solution(object):
    def sortList(self, head):
        """
        merge sort
        :type head: ListNode
        :rtype: ListNode
        """

        # corner case but also divide termination
        if head == None or head.next == None:
            return head

        # divide
        first, second = head,head.next
        while second != None and second.next != None:
            first = first.next
            second = second.next.next
        second = first.next

        # cut into 2 pieces started with head and second
        first.next = None

        l = self.sortList(head)
        r = self.sortList(second)

        return self.merge(l,r)


    def merge(self, l, r):
        """
        merge two sorted list
        :type l: ListNode
        :type r: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        p = head
        while l != None and r != None:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        if l != None:
            p.next = l
        if r != None:
            p.next = r
        return head.next

if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(4)
    c = ListNode(1)
    d = ListNode(10)
    a.next = d
    d.next = c
    c.next = b

    s = Solution()
    a = s.sortList(a)
    print_list(a)






