class solution(object):
    def __init__(self):
        pass

    def validaterow(self, board, index):
        collect = set()
        for letter in range(9):
            item = board[index][letter]
            if item.isdigit():
                if item in collect:
                    return False
            else:
                collect.add(item)
        return True

    def validatecolumn(self, board, index):
        collect = set()
        for letter in range(9):
            item = board[letter][index]
            if item.isdigit():
                if item in collect:
                    return False
                else:
                    collect.add(item)
        return True

    def validateCell(self, board, index_i, index_j):
        collect = set()
        for i in range(3):
            for j in range(3):
                item = board[index_i + i][index_j + j]
                if item.isdigit():
                    if item in collect:
                        return False
                    else:
                        collect.add(item)
        return True

    def isValid(self, board):
        for i in range(9):
            if not self.validaterow(board, i):
                return False
            if not self.validatecolumn(board, i):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.validateCell(board, i, j):
                    return False
        return True

mysol = solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".","2","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print("Is this sudoku valid??")

ans = mysol.isValid(board)
if ans:
    print("yes it is")
else:
    print("oops no")
