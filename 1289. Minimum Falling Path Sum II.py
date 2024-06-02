from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
import heapq
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        if (len(grid[0]) == 1):
            return grid[-1][-1]
        n = len(grid[0])
        current = sorted([(grid[0][i], i) for i in range(n)])
       
        for i in range(1, len(grid)):
            next = []
            
            for j in range(n):
                if current[0][1] == j:
                    v = current[1][0]
                else:
                    v = current[0][0]
                next.append(v + grid[i][j])
            current = sorted([(next[i], i) for i in range(n)])
        return current[0][0]
start_time = time.time()
app = Solution()
root = app.minFallingPathSum([[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


