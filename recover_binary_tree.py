# https://leetcode.com/problems/recover-binary-search-tree/solution/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkbound(self, node, rparent, lparent):
        wrong_items = set()
        if node.left:
            if node.left.val > node.val:
                wrong_items.add(node.left)
                wrong_items.add(node)
            if rparent and node.val < rparent.val:
                wrong_items.add(node)
                wrong_items.add(rparent)
            if lparent and node.val > lparent.val:
                wrong_items.add(node)
                wrong_items.add(lparent)

            wrong_items = wrong_items.union(self.checkbound(node.left, rparent.val, node.val))

        if node.right:
            if node.right.val < node.val or node.right.val < rparent.val or node.right.val > lparent.val:
                return node.right
            else:
                wrong_item = self.checkbound(node.right, node.val, lparent.val)

        return wrong_item

    def validspot(self, node, value):
        if node.left and node.left.val > value:
            return False
        if node.right and node.right.val < value:
            return False

        return True

    def findNode(self, root, wrong_item):
        value = wrong_item.val

        itr = root
        while not (self.validspot(itr, value)):
            if itr.left and value < itr.left.val:
                itr = itr.left
            if itr.right and value > itr.right.val:
                itr = itr.right

        return itr

    def recoverTree(self, root):
        INF = 2 ** 31 - 1
        NINF = -2 ** 31

        wrong_item = root
        while wrong_item != None:
            wrong_item = self.checkbound(root, None, None)

            if wrong_item == None:
                return
            right_place_for_it = self.findNode(root, wrong_item)
            temp = right_place_for_it.val
            right_place_for_it.val = wrong_item.val
            wrong_item.val = temp

        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
