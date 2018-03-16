# coding:utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        if head.next == None:
            return head
        
        p1 = head # front of p2
        p2 = head.next #current node to insert
        p3 = head # node to swap
        p4 = head # front of p3
        while p2 != None:

            print p2.val
            p3 = head
            p4 = None
            while p3 != p2:
                print " " + str(p3.val)
                if p3.val > p2.val:
                    #insert p2 in front of p3
                    if p4 == None:
                        # p3 is head
                        p1.next = p3
                        temp = p3.next
                        p3.next = p2.next
                        p2.next = temp
                        head = p2
                        p2 = p3
                    else:
                        # p3 is not head
                        p4.next = p2
                        temp = p2.next
                        p2.next = p3.next
                        p1.next = p3
                        p3.next = temp
                        p2 = p3
                    break
                else:
                    p4 = p3
                    p3 = p3.next
            p1 = p2
            p2 = p2.next
            # print p2.val
        return head

if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(4)
    c = ListNode(1)
    a.next = b
    b.next = c
    # print a.next.val
    s = Solution()
    a = s.insertionSortList(a)
    print a.val,a.next.val,a.next.next.val