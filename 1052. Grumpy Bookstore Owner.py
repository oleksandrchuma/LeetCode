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
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total = 0
        best_saved = 0
        saved = 0
        for i in range(len(customers)):
            if grumpy[i]==0:
                total += customers[i]
            else:
                saved += customers[i]
            if i >= minutes and grumpy[i-minutes]==1:
                saved -= customers[i-minutes]
            if (saved > best_saved):
                best_saved = saved
        return total+best_saved
                
start_time = time.time()
t = Solution()
root = t.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
