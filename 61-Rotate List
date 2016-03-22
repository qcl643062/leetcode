"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        length = 0
        head1 = head
        while head1.next:
            length += 1
            head1 = head1.next
        length = length + 1
        k1 = k % length
        if k == 0 or k1 == 0:
            return head
        head2 = head
        head1.next = head2
        for i in range(length - k1 -1):
            head2 = head2.next
        head = head2.next
        head2.next = None
        return head
s = Solution()
ListNode1 = s.rotateRight(ListNode(1, ListNode(0, ListNode(2, ListNode(3)))), 2)
while ListNode1:
    print ListNode1.val
    ListNode1 = ListNode1.next