# https://leetcode.com/problems/maximal-rectangle/

class Solution(object):
    def maximalRectangle(self, matrix):
        def ht(i, j, upper):
            itr = i
            while itr < upper and matrix[itr][j] == "1":
                itr += 1
            return itr - 1

        rows = len(matrix)
        if rows == 0:
            return 0
        cols = len(matrix[0])

        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    continue
                height = ht(i, j, rows)
                area = height - i + 1
                jj = j + 1

                while jj < cols and matrix[i][jj] == "1":
                    height = ht(i, jj, height + 1)
                    if area < (height - i + 1) * (jj - j + 1):
                        area = (height - i + 1) * (jj - j + 1)
                    jj += 1

                if max_area < area:
                    max_area = area

        return max_area

        """
        :type matrix: List[List[str]]
        :rtype: int
        """
