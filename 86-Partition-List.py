"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""
class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        listofnode = []
        while head:
            listofnode.append(head)
            head = head.next
        listofnode1 = []
        listofnode2 = []
        for i in xrange(len(listofnode)):
            if listofnode[i].val < x:
                listofnode1.append(listofnode[i])
            else:
                listofnode2.append(listofnode[i])
        listofnode1.extend(listofnode2)
        for i in xrange(len(listofnode1) - 1):
            listofnode1[i].next = listofnode1[i + 1]
        listofnode1[-1].next = None
        return listofnode1[0]
s = Solution()
m = s.partition(ListNode(2,ListNode(3, ListNode(1))), 2)
while m:
    print m.val
    m = m.next