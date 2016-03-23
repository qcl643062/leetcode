"""
Reverse a singly linked list.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        head2 = head
        head1 = head.next
        while head1 != None:
            head.next = head1.next
            head1.next = head2
            head2 = head1
            head1 = head.next
        return head2
s = Solution()
slist = s.reverseList(ListNode(0, ListNode(1)))
while slist:
    print slist.val
    slist = slist.next