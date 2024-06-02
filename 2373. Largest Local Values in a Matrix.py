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
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = [[0 for _ in range(n-2)] for _ in range(n-2)]
        for row in range(1, n-1):
            for col in range(1, n-1):
                result[row-1][col-1] = max([grid[row+dr][col+dc] for dr in range(-1, 2) for dc in range(-1, 2)])
        return result
start_time = time.time()
t = Solution()
root = t.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])
pprint.pprint(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
