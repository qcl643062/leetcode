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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        a = []
        def poster(root):
            if root == None:
                return []
            if root.left != None:
                poster(root.left)
            if root.right != None:
                poster(root.right)
            a.append(root.val)
        poster(root)
        return a
s = Solution()
print s.postorderTraversal(TreeNode(0, TreeNode(1, TreeNode(2)), TreeNode(3)))