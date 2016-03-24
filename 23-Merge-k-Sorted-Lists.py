"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return None
        if len(lists) == 1:
            return lists[0]
        list1 = []
        for i in lists:
            while i:
                list1.append(i.val)
                i = i.next
        if list1 == []:
            return None
        else:
            a = ListNode(None)
            b = a
            list1.sort()
            for i in range(len(list1)):
                if i != len(list1) - 1:
                    b.val = list1[i]
                    b.next = ListNode(None)
                    b = b.next
                else:
                    b.val = list1[i]
            return a
s = Solution()
m = s.mergeKLists([ListNode(1,ListNode(2, ListNode(3))), ListNode(2)])
while m:
    print m.val
    m = m.next