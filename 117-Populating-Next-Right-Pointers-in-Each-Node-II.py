"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""

class TreeLinkNode(object):
    def __init__(self, x, left = None, right = None, next = None):
        self.val = x
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return root 
        a = [root]
        b = []
        while a != []:
            for i in a:
                if i.left:
                    b.append(i.left)
                if i.right:
                    b.append(i.right)
            if b != []:
                for i in range(len(b) - 1):
                    b[i].next = b[i + 1]
            a = b
            b = []