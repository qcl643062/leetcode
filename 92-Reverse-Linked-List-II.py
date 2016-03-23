#coding=utf-8
"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""

class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        if not head.next:
            return head
        if m == n:
            return head
        head1 = head
        length = 0 
        while head1:
            length += 1
            head1 = head1.next
        listofnode = []
        head1 = head
        if m == 1:
            for i in xrange(n):
                listofnode.append(head1)
                head1 = head1.next
            for i in xrange(len(listofnode) - 1):
                listofnode[i + 1].next = listofnode[i]
            listofnode[0].next = head1
            return listofnode[-1]
        if m > 1:
            for i in xrange(m - 2):
                head1 = head1.next
            head2 = head1.next
            for i in xrange(n - m + 1):
                listofnode.append(head2)
                head2 = head2.next
            for i in xrange(len(listofnode) - 1):
                listofnode[i + 1].next = listofnode[i]
            head1.next = listofnode[-1]
            listofnode[0].next = head2
            return head
s = Solution()
m = s.reverseBetween(ListNode(3, ListNode(5)), 1, 2)
while m:
    print m.val
    m = m.next