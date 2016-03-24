"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST
"""

class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        listofall = []
        while head:
            listofall.append(head.val)
            head = head.next
        def sortedArrayToBST(nums):
            length = len(nums)
            if length == 0:
                return None
            if length == 1:
                return TreeNode(nums[0])
            if length == 2:
                root = TreeNode(nums[0])
                root.right = TreeNode(nums[1])
            if length == 3:
                root = TreeNode(nums[1])
                root.left = TreeNode(nums[0])
                root.right = TreeNode(nums[2])
                return root
            root = TreeNode(nums[length / 2])
            root.left = sortedArrayToBST(nums[:length / 2])
            root.right = sortedArrayToBST(nums[length / 2 + 1:])
            return root
        return sortedArrayToBST(listofall)
s = Solution()
print s.sortedListToBST(ListNode(0, ListNode(1, ListNode(2))))