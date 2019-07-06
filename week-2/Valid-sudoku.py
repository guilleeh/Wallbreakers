from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d = defaultdict(int)
        board_blocks = []
        for i in range(len(board)):
            row_set = set()
            column_set = set()
            for j in range(len(board[i])):
                row_cell = board[i][j]
                column_cell = board[j][i]
                if row_cell in row_set or column_cell in column_set:
                    return False
                else:
                    if row_cell != ".":
                        row_set.add(row_cell)
                    if column_cell != ".":
                        column_set.add(column_cell)

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                d.clear()
                for x in range(3):
                    for y in range(3):
                        if board[i + x][j + y] != ".":
                            d[board[i + x][j + y]] += 1
                            if (d[board[i + x][j + y]]) > 1:
                                return False

        return True
