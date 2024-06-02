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
import numpy 
import pprint

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[-1][-1] == 1: 
            return 0
        thiefs = [(row, col) for row in range(n) for col in range(n) if grid[row][col] == 1]
        proceed = True
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        level = 1
        
        while proceed:
            next = []
            level += 1
            for row,col in thiefs:
                for dr, dc in dirs:
                    nr = row + dr 
                    nc = col + dc
                    if nr >= 0 and nc >= 0 and nr < n and nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = level
                        next.append((nr,nc))
            proceed = len(next) > 0
            thiefs = next

        pprint.pprint(grid)
        heap = []
        heapq.heappush(heap, (-grid[0][0], (0,0)))
        visited = set()
        visited.add((0,0))
        while heap:
            level, pos = heapq.heappop(heap)
            row, col = pos
            if row == n-1 and col == n-1:
                return -level
            for dr, dc in dirs:
                nr = row + dr 
                nc = col + dc
                if nr >= 0 and nc >= 0 and nr < n and nc < n and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    heapq.heappush(heap, (-min(-level, grid[nr][nc]), (nr,nc)))
        return 1
start_time = time.time()
t = Solution()
root = t.maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
