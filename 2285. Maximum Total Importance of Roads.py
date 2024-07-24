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
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        nums = [0]*n
        for road in roads: 
            nums[road[0]] += 1
            nums[road[1]] += 1
        ordered = sorted([(val, ind) for ind, val in enumerate(nums)])
        vals = [0]*n
        i = 1
        for vertix in ordered:
            vals[vertix[1]] = i
            i += 1
        return sum([vals[road[0]]+vals[road[1]] for road in roads])
            
start_time = time.time()
t = Solution()
root = t.maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
