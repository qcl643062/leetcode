"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number 
and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...
"""

class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        if not head.next:
            return head
        n = 2
        RightOdd = head
        LeftEven = head.next
        RightEven = head.next
        head1 = head.next.next
        while head1:
            n = n + 1
            if n % 2 == 0:
                RightEven.next = head1
                RightEven = head1
                head1 = head1.next
            else:
                RightEven.next = head1.next
                RightOdd.next = head1
                head1.next = LeftEven
                RightOdd = head1
                head1 = RightEven.next
        return head
s = Solution()
m = s.oddEvenList(ListNode(2,ListNode(2, ListNode(1))))
while m:
    print m.val
    m = m.next