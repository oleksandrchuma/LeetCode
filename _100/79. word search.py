from typing import List
from typing import Optional
import time
from collections import Counter
import math
class Solution:
    def doStep(self, board: List[List[str]], word: str, used: List[List[int]], row, col, index) -> bool:
        if index == len(word):
            return True
        
        if row > 0 and used[row-1][col] == 0 and board[row-1][col]== word[index]:
            used[row-1][col] = 1
            if (self.doStep(board, word, used, row-1, col, index+1)):
                return True
            used[row-1][col] = 0
        if row + 1 < len(board) and used[row+1][col] == 0 and board[row+1][col]== word[index]:
            used[row+1][col] = 1
            if (self.doStep(board, word, used, row+1, col, index+1)):
                return True
            used[row+1][col] = 0
        if col > 0 and used[row][col-1] == 0 and board[row][col-1]== word[index]:
            used[row][col-1] = 1
            if (self.doStep(board, word, used, row, col-1, index+1)):
                return True
            used[row][col-1] = 0
        if col + 1 < len(board[0]) and used[row][col+1] == 0 and board[row][col+1]== word[index]:
            used[row][col+1] = 1
            if (self.doStep(board, word, used, row, col+1, index+1)):
                return True
            used[row][col+1] = 0

        return False 
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0:
            return False
        if word == '':
            return True        
        m = len(board[0])
        n = len(board)
        used = [[0] * m for i in range(n)]
        for row in range(n):
            for col in range(m):
                if board[row][col] == word[0]:
                    used[row][col] = 1
                    if self.doStep(board, word, used, row, col, 1):
                        return True
                    used[row][col] = 0
                    
        return False             
start_time = time.time()
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

