"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        list1 = head
        p = list1.val
        while list1.next != None:
            if list1.next.val == p:
                list1.next = list1.next.next
                continue
            else:
                p = list1.next.val
                list1 = list1.next
        return head
s = Solution()
m = s.deleteDuplicates(ListNode(2,ListNode(2, ListNode(1))))
while m:
    print m.val
    m = m.next
