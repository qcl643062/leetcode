"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            if head.next:
                b = head.next
                head.next = head.next.next
                b.next = head
                head = b
                left = head.next
                while left.next and left.next.next:
                    b = left.next
                    left.next = b.next
                    c = left.next.next
                    left.next.next = b
                    b.next = c
                    left = left.next.next
        return head
s = Solution()
ListNode1 = s.swapPairs(ListNode(1, ListNode(0, ListNode(2, ListNode(3)))))
while ListNode1:
    print ListNode1.val
    ListNode1 = ListNode1.next