# coding:utf-8

#Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return self.divideAndMerge(lists, 0, len(lists) - 1)
    def divideAndMerge(self, lists, begin, end):
        """
        进行递归

        """
        if begin > end:
            return lists
        # base
        if begin == end:
            return lists[begin]
        # divide
        mid = (begin + end) / 2
        
        l = self.divideAndMerge(lists, begin, mid)
        r = self.divideAndMerge(lists, mid+1, end)
        return self.merge(l, r)

    def merge(self, l, r):
        """
        :type l: ListNode
        :type r: ListNode
        :rtype ListNode
        """
        p = head = ListNode(0)
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
        else:
            p.next = r
        return head.next