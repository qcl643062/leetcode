"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
"""

class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        def preorder(root):
            if not root:
                return root
            stack.append(root)
            if root.left:
                preorder(root.left)
            if root.right:
                preorder(root.right)
            return stack
        preorder(root)
        for i in range(len(stack) - 1):
            stack[i].left = None
            stack[i].right = stack[i + 1] 