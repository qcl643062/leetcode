#coding=utf-8
"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.
Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA:
            return None
        if not headB:
            return None
        lenofheadA = 0
        lenofheadB = 0
        headB1 = headB
        headA1 = headA
        while headB1:
            lenofheadB += 1
            headB1 = headB1.next
        while headA1:
            lenofheadA += 1
            headA1 = headA1.next
        deviation = abs(lenofheadA - lenofheadB)
        if lenofheadA >= lenofheadB:
            for i in range(deviation):
                headA = headA.next
            NumofStep = 0
            while NumofStep < lenofheadB:
                if headA == headB:
                    return headB
                else:
                    headB = headB.next
                    headA = headA.next
                NumofStep += 1
            else:
                return None
        else:
            for i in range(deviation):
                headB = headB.next
            NumofStep = 0
            while True:
                if headA == headB:
                    return headB
                else:
                    headB = headB.next
                    headA = headA.next
                NumofStep += 1
            else:
                return None


