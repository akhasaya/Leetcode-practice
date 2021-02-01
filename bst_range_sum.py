# add all numbers in a bst, add the values that fall in [low,high]
# here i checked every node, but ideally, if a node value is less than low, no need to check the left branch, as all values in left will be even lessar

# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        if root == None:
            return 0

        stack = [root]
        total = 0
        while len(stack) > 0:
            node = stack.pop()
            if low <= node.val <= high:
                total += node.val
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return total
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
