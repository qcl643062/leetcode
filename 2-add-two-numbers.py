"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order 
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        l11 = l1
        odd = 0
        if l11.next or l2.next:
            digitalsum = l2.val + odd + l11.val
            odd = digitalsum / 10
            l11.val = digitalsum % 10
            while l11.next or l2.next:
                if not l11.next:
                    if l2.next.val + odd < 10:
                        l2.next.val += odd
                        l11.next = l2.next
                        return l1
                    else:
                        l2.next.val = l2.next.val + odd - 10
                        odd = 1
                        l11.next = l2.next
                        l11 = l11.next
                        while l11.next:
                            digitalsum = l11.next.val + odd
                            odd = digitalsum / 10
                            l11.next.val = digitalsum % 10                            
                            l11 = l11.next
                        if odd == 1:
                            l11.next = ListNode(1)
                        return l1
                if not l2.next:
                    l11.next.val += odd
                    if l11.next.val < 10:
                        return l1
                    else:
                        l11.next.val += -10
                        odd = 1
                        l11 = l11.next
                        while l11.next:
                            digitalsum = l11.next.val + odd
                            odd = digitalsum / 10
                            l11.next.val = digitalsum % 10
                            
                            l11 = l11.next
                        if odd == 1:
                            l11.next = ListNode(1)
                        return l1
                else:
                    digitalsum = l2.next.val + l11.next.val + odd
                    odd = digitalsum / 10
                    l11.next.val = digitalsum % 10
                    
                    l11 = l11.next
                    l2 = l2.next
            else:
                if odd == 1:
                    l11.next = ListNode(1)
                return l1
                    
        else:
            l11.val += l2.val + odd
            if l11.val >= 10:
                l11.val += -10
                l11.next = ListNode(1)
                return l1
            else:
                return l1

s = Solution()
resu = s.addTwoNumbers(ListNode(9, ListNode(8)), ListNode(1))
while resu:
    print resu.val
    resu = resu.next



