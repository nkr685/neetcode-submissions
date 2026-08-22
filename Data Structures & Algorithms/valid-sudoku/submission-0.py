class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = []
        for i in range(9):
            col = []
            for j in range(9):
                cell = board[i][j] 
                if cell != '.':
                    if cell not in col:
                        col.append(cell)
                    else:
                        return False
        for i in range(9):
            col = []
            for j in range(9):
                cell = board[j][i] 
                if cell != '.':
                    if cell not in col:
                        col.append(cell)
                    else:
                        return False

        for coord in [(0,0),(3,0), (6,0), (0,3), (3,3), (6,3), (6,0), (6,3), (6,6)]:
            x = coord[0]
            y = coord[1]
            square = []
            for i in range(3):
                for j in range(3):
                    cell = board[x+i][y+j] 
                    if cell != '.':
                        if cell not in square:
                            square.append(cell)
                        else:
                            return False
        return True





