from typing import List
from typing import Optional
import time
import math
class Solution:
    val = {'1','2','3','4','5','6','7','8','9'}
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        cells = [(i,j, self.getPossibleVal(board, i, j)) for i in range(9) for j in range(9) if board[i][j] == '.']
        cells = sorted(cells, key=lambda x: len(x[2]))
        k = 0
        reverse = False
        while (k < len(cells)):
            (i, j, dic) = cells[k]
            if (not(reverse)):
                dic = self.getPossibleVal(board, i, j)
                cells[k] = (i, j, dic)
            

            if (len(dic) == 0):
                board[i][j] = '.'
                reverse = True
                k -= 1
            else:
                reverse = False
                k += 1
                board[i][j] = dic.pop() 
#        self.printTable(board, 9, 9)

    def printTable(self, board, num_rows, num_columns):
        for i in range(num_rows):
            for j in range(num_columns):
                cell_value = board[i][j]
                print(cell_value.ljust(1), end="  ")
            print()    

    def getPossibleVal(self, board, i, j):
        r = self.getRow(board, i)
        c = self.getCol(board, j)
        cell = self.getCellSet(board, i//3, j//3)
        return (self.val - r) & (self.val - c) & (self.val - cell)    
    
    def getCell(self, board, i, j) -> List[List[int]]:
        return [r[3*j:3*(j+1)] for r in board[3*i:3*(i+1)]]  
    
    def getCellSet(self, board, i, j) -> set[str]:
        return set(board[i*3+x][j*3+y] for x in range(3) for y in range(3) if board[i*3+x][j*3+y] != '.')  

    def getRow(self, board, i) -> set[str]:
        return set(x for x in board[i] if x != '.')  
    
    def getCol(self, board, j) -> set[str]:
        return set(board[i][j] for i in range(9) if board[i][j] != '.')
    

start_time = time.time()
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

Solution().solveSudoku(board)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
