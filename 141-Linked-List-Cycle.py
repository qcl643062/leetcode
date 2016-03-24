"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        if not head.next:
            return False
        twostep = head.next.next
        while True:
            if head.next == twostep:
                return True
            else:
                head = head.next
                if not twostep:
                    return False
                elif not twostep.next:
                    return False
                else:
                    twostep = twostep.next.next
s = Solution()
print s.hasCycle(ListNode(0, ListNode(1)))