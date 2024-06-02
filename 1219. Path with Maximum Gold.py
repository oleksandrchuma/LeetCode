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
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        max_val = 0
        m = len(grid[0])
        n = len(grid)
        step = [[[] for _ in range(m)] for _ in range(n)]
        dirs = [[[] for _ in range(m)] for _ in range(n)]
        proceed = False
        full = True
        for row in range(n):
            max_val = max(max_val, max(grid[row]))
            for col in range(m):
                if grid[row][col] > 0:
                    proceed = True
                    zero = 0
                    if row > 0:
                        if grid[row-1][col] > 0:
                            dirs[row][col].append((-1,0))
                        else: 
                            zero = 1
                    if col > 0:
                        if grid[row][col-1] > 0:
                            dirs[row][col].append((0,-1))
                        else:
                            zero = 1
                    if row < n-1:
                        if grid[row+1][col] > 0:
                            dirs[row][col].append((1,0))
                        else:
                            zero = 1 
                    if col < m-1:
                        if grid[row][col+1] > 0:
                            dirs[row][col].append((0,1))
                        else: 
                            zero = 1
                    if zero:
                        full = False
                        step[row][col] =[(grid[row][col], {row*m+col})]    
        if full:
            return sum([sum(grid[row]) for row in range(n)])
        while proceed:
            proceed = False
            next_step = [[[] for _ in range(m)] for _ in range(n)]
            for row in range(n):
                for col in range(m):
                    if grid[row][col] > 0:
                        index = row*m+col
                        for dr, dc in dirs[row][col]:
                            for val, path in step[row+dr][col+dc]:
                                if index not in path:
                                    new_path = set(list(path)+[index])
                                    new_val = val + grid[row][col]
                                    if new_val > max_val:
                                        max_val = new_val
                                    next_step[row][col].append((new_val, new_path))
                                    proceed = True
            step = next_step
        return max_val
start_time = time.time()
t = Solution()
root = t.getMaximumGold([[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
