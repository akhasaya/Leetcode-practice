# rotate a matrix clockwise by 90 degrees

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        print(matrix)
        for i in range(n / 2):
            for j in range(i, n - i - 1):
                # print("round 1")
                # print(matrix[i][j], matrix[n - i - 1][j], matrix[n - i - 1][n - j - 1], matrix[i][n - j - 1])
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = tmp
                print(matrix)

        return matrix
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
