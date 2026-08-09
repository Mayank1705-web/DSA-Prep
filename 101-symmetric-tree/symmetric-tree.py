# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mirror(self, left, right):
        if right is None and left is None:
            return True
        
        if right is None or left is None:
            return False
        
        if right.val != left.val:
            return False

        leftNodes = self.mirror(left.left, right.right)
        rightNodes = self.mirror(right.left, left.right)

        return leftNodes and rightNodes

    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        return self.mirror(root.left, root.right)