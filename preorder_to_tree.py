# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def process(self, S, l):
        answer = []
        spt = S.split("-")
        answer.append(spt[0])
        if len(spt) < 2:
            return answer
        count = 1
        for i in spt[1:]:
            if i == "":
                count += 1
            else:
                answer.append(count)
                answer.append(i)
                count = 1

        return answer

    def recoverFromPreorder(self, S):
        l = len(S)
        if l < 1:
            return None

        processed = self.process(S, l)

        stack = []
        stack.append(TreeNode(int(processed[0])))

        for i in processed[1:]:
            if isinstance(i, int):
                count = i

            else:
                while len(stack) > count:
                    stack.pop()

                last_node = stack[-1]

                if last_node.left == None:
                    new_node = TreeNode(int(i))
                    last_node.left = new_node
                    stack.append(new_node)
                else:
                    new_node = TreeNode(int(i))
                    last_node.right = new_node
                    stack.append(new_node)

        return stack[0]

        """
        :type S: str
        :rtype: TreeNode
        """
