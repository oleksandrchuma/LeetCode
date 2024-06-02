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
    def subsetXORSum(self, nums: List[int]) -> int:
        res = [0]
        for num in nums: 
            res = res + [x^num for x in res]
        return sum(res)
start_time = time.time()
t = Solution()
root = t.subsetXORSum( [1,3])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
