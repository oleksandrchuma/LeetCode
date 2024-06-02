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
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        kids = []
        min_h = 0 
        for h in happiness:
            if len(kids) < k or h > min_h:
                heapq.heappush(kids, h)

                if len(kids) > k:
                    min_h = heapq.heappop(kids)
        while len(kids) > min_h:
            min_h = heapq.heappop(kids)
            if min_h > len(kids):
                heapq.heappush(kids, min_h)
        return sum(kids)-len(kids)*(len(kids)-1)//2
start_time = time.time()
t = Solution()
root = t.maximumHappinessSum([2,3,4,5],4)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
