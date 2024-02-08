from typing import List
from typing import Optional
import time
from collections import Counter

# Definition for a binary tree node.
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        if n <= 2 or m <= 2:
            return 
        for col in range(m):
            if board[0][col] == 'O':
                self.bfs(board, 0, col)
            if board[n-1][col] == 'O':
                self.bfs(board, n-1, col)
        
        for row in range(n):
            if board[row][0] == 'O':
                self.bfs(board, row, 0)
            if board[row][m-1] == 'O':
                self.bfs(board, row, m-1)
        for row in range(n):
            for col in range(m):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'F':
                    board[row][col] = 'O'

    def bfs(self, board, row, col):
        n = len(board)
        m = len(board[0])
        stack = [(row,col)]
        board[row][col] = 'F'
        while (stack):
            r, c = stack.pop()
            if (r > 0 and board[r-1][c] == 'O'):
                board[r-1][c] = 'F'
                stack.append((r-1, c))
            if (r < n-1 and board[r+1][c] == 'O'):
                board[r+1][c] = 'F'
                stack.append((r+1, c))
            if (c > 0 and board[r][c-1] == 'O'):
                board[r][c-1] = 'F'
                stack.append((r, c-1))
            if (c < m-1 and board[r][c+1] == 'O'):
                board[r][c+1] = 'F'
                stack.append((r, c+1))

start_time = time.time()
app = Solution()
m = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]   
root = app.solve(m)
print(m)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
