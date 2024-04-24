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
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        fact = [2,3,5]
        heap = [1]
        u = {1}
        heapq.heapify(heap)
        i = 1
        while i < n:
            x = heapq.heappop(heap)
            for f in fact:
                y = f*x 
                if y not in u:
                    u.add(y)
                    heapq.heappush(heap, y)
            i+=1
        return heapq.heappop(heap)   
start_time = time.time()
t = Solution()
root = t.nthUglyNumber(10)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
