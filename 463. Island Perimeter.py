import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
from queue import Queue
import math
import itertools
import heapq
from collections import Counter
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dirs = [(1,0), (0, 1), (-1,0), (0, -1)]
        res = 0
        n = len(grid)
        m = len(grid[0])
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 0:
                    continue
                res += 4
                for d in dirs:
                    dx = row+d[0]
                    dy = col+d[1]
                    if dx>=0 and dy>=0 and dx < n and dy < m and grid[dx][dy] == 1:
                        res-=1
        return res 
start_time = time.time()
t = Solution()
root = t.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
