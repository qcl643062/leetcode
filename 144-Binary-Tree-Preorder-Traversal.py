"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        a = []
        def preorder(root):
            if root == None:
                return []
            a.append(root.val)
            if root.left != None:
                preorder(root.left)
            if root.right != None:
                preorder(root.right)
        preorder(root)
        return a
s = Solution()
print s.preorderTraversal(TreeNode(0, TreeNode(1, TreeNode(2)), TreeNode(3)))