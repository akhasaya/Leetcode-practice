# https://leetcode.com/explore/interview/card/google/62/recursion-4/399
class Solution(object):
    def findInner(self, n):
        if n == 1:
            return ["0", "1", "8"]
        if n == 2:
            return ["00", "11", "69", "88", "96"]

        seq = self.findInner(n - 2)
        l = len(seq[0])
        array = ["00", "11", "69", "88", "96"]
        result = []

        for elem in seq:
            for border in array:
                result.append(
                    border[0] + elem + border[1]
                )

        return result

    def findStrobogrammatic(self, n):
        if n == 1:
            return ["0", "1", "8"]
        if n == 2:
            return ["11", "69", "88", "96"]

        seq = self.findInner(n - 2)
        l = len(seq[0])
        array = ["11", "69", "88", "96"]
        result = []

        for elem in seq:
            for border in array:
                result.append(
                    border[0] + elem + border[1]
                )

        return result
        """
        :type n: int
        :rtype: List[str]
        """
