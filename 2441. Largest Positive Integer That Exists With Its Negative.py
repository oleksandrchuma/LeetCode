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
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d = defaultdict(int)
        res = -1
        for num in nums:
            anum = abs(num)
            if anum > res and anum in d and d[anum]+num == 0:
                res = anum
            elif anum not in d:
                d[anum] = num 
        return res
start_time = time.time()
t = Solution()
root = t.findMaxK([-1,10,6,7,-7,1])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
