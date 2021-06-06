from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> None:
        for i in range(9):
            row = {}
            col = {}
            block = {}
            row_cube = 3* (i//3)
            col_cube = 3* (i%3)
            for j in range(9):
                if board[i][j] !='.' and board[i][j] in row:
                    return False # which means invalid
                row[board[i][j]] = 1
                if board[j][i] != '.' and board[j][i] in col:
                    return False
                col[board[j][i]] = 1
                rc = row_cube + j // 3
                cc = col_cube + j % 3
                if board[rc][cc] in block and board[rc][cc] != '.':
                    return False
                block[board[rc][cc]] = 1
        return True

sln = Solution()
a = [[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
print(sln.isValidSudoku(a))
b = [["abc",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
print(sln.isValidSudoku(b))