# if matrix is
"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]

 diagonally go up, 1
 diagonally go down 2 4
 diagonally move up 7 5 3
 then down    6 8
 then up 9

 answer = [1,2,4,7,5,3,6,8,9]
"""
class Solution(object):
    def findDiagonalOrder(self, matrix):
        row = len(matrix)
        if row < 1:
            return []
        col = len(matrix[0])
        if col < 1:
            return []

        answer = []
        i, j = 0, 0

        while True:
            answer.append(matrix[i][j])
            if i == row - 1 and j == col - 1:
                break

            if (i + j) % 2 == 0:
                # move up
                if i == 0 and j + 1 < col:
                    j = j + 1
                elif j == col - 1 and i + 1 < row:
                    i = i + 1
                else:
                    i, j = i - 1, j + 1

            else:
                # move down
                if i == row - 1 and j + 1 < col:
                    j = j + 1
                elif j == 0 and i + 1 < row:
                    i = i + 1
                else:
                    i, j = i + 1, j - 1

        return answer

        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
