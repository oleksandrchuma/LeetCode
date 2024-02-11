from typing import List
from typing import Optional
import time
from collections import Counter
from functools import lru_cache

class Solution:
    def doStep(self, state, row):
        dir = [(i, j) for i in range(-1, 2) for j in range(-1,2)]
        n = len(row)
        res = [[-1 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                m = row[i]+row[j]-(row[j] if i == j else 0)
                maxval = max([state[i+di][j+dj] for (di,dj) in dir 
                              if (i+di < n and j+dj < n and i+di>=0 and j+dj>=0 
                                  and state[i+di][j+dj] != -1)], default=-1)
                res[i][j] = maxval+m if maxval != -1 else -1
        return res 
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        state = [[-1 for _ in range(n)] for _ in range(n)]
        state[0][n-1] = grid[0][0] + grid[0][n-1]
        for row in range(1,len(grid)):
            state = self.doStep(state,grid[row])
           # print(f"Step {row}")
           # self.print_matrix(state)
        return max(state[i][j] for i in range(n) for j in range(n))
    def print_matrix(self, matrix):
        max_width = 2
        for row in matrix:
            print(" ".join(f"{element:>{max_width}}" for element in row))


start_time = time.time()
app = Solution()
data = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
root = app.cherryPickup(data)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

