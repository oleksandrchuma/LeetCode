import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import heapq
from collections import Counter

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def fill(row, col):
            if row >= 0 and row < n and col >= 0 and col < m and grid[row][col] == "1":
                grid[row][col] = "0"
                fill(row+1,col)
                fill(row-1,col)
                fill(row,col+1)
                fill(row,col-1)
        n = len(grid)
        m = len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    fill(i, j)
                    res += 1
        return res                 
start_time = time.time()
app = Solution()
root = app.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])

#root = app.calculateMinimumHP([[0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

