#https://leetcode.com/problems/binary-tree-maximum-path-sum/
#solved a hard problem on my own

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.localmax = []
        self.INF = 10

    def findMaxPartialandFullSum(self, node):
        if node == None:
            return -1 * self.INF

        if node.left:
            left = self.findMaxPartialandFullSum(node.left)
        else:
            left = -1 * self.INF
        if node.right:
            right = self.findMaxPartialandFullSum(node.right)
        else:
            right = -1 * self.INF

        m = max(left, right, node.val, left + node.val, right + node.val, left + node.val + right)
        self.localmax.append(m)

        if node.left:
            if node.right:
                return max(node.val + left, node.val + right, node.val)
            else:
                return max(node.val + left, node.val)
        else:
            if node.right:
                return max(node.val + right, node.val)
            else:
                return node.val

    def maxPathSum(self, root):
        if root == None:
            return 0

        if root.left == None and root.right == None:
            return root.val

        self.localmax.append(self.findMaxPartialandFullSum(root))

        return max(self.localmax)

        """
        :type root: TreeNode
        :rtype: int
        """
