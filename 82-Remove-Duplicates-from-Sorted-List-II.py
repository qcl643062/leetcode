"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
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
        if not head:
            return head
        if not head.next:
            return head
        if head.val == head.next.val:
            a = head.val
            head = head.next.next
            head1 = head
            while head1:
                if head1.val == a:
                    head = head1.next
                    head1 = head1.next
                else:
                    head = head1
                    a = head.val
                    head1 = head1.next
                    if head.next:
                        if head.next.val != a:
                            break
        if head:
            head2 = head
            head1 = head.next
            while head1:
                if head1.next:
                    if head1.next.val == head1.val:
                        a = head1.val
                        while head1:
                            if head1.val == a:
                                head1 = head1.next
                            else:
                                head2.next = head1
                                break
                        else:
                            head2.next = head1
                            break
                    else:
                        head2 = head2.next
                        head1 = head1.next
                else:
                    break
        return  head
s = Solution()
m = s.deleteDuplicates(ListNode(2,ListNode(2, ListNode(1))))
while m:
    print m.val
    m = m.next