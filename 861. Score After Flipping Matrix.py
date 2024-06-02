from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
import heapq
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            if grid[row][0] == 0:
                for col in range(len(grid[row])):
                    grid[row][col] = 0 if grid[row][col] else 1
        for col in range(1, len(grid[0])):
            if sum([grid[row][col] for row in range(len(grid))]) <= len(grid)//2:
                for row in range(len(grid)):
                    grid[row][col] = 0 if grid[row][col] else 1
        res = 0
        for row in range(len(grid)):
            res += int(''.join(str(v) for v in grid[row]), 2)
        return res 
start_time = time.time()
app = Solution()
root = app.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


