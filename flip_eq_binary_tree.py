# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/flip-equivalent-binary-trees/
class Solution(object):
    def flipEquiv(self, root1, root2):
        if root1 == None and root2 == None:
            return True

        if root1 == None or root2 == None:
            return False

        if root1.val != root2.val:
            return False

        l1 = root1.left.val if root1.left != None else None
        l2 = root2.left.val if root2.left != None else None

        r1 = root1.right.val if root1.right != None else None
        r2 = root2.right.val if root2.right != None else None

        if l1 == l2 and r1 == r2:
            answer = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
            if answer == True:
                return True

        if l1 == r2 and r1 == l2:
            return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)

        return False

        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
