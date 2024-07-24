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
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1: 
            return 1 
        primes.sort()
        heap = []
        for i in range(len(primes)):
            heapq.heappush(heap, (primes[i], i))
        
        i = 2
        num = 0
        while True:
            num, index = heapq.heappop(heap)
            if i == n:
                break
            i += 1
            for j in range(index+1):
                heapq.heappush(heap, (num*primes[j], j))
            
        return num
start_time = time.time()
t = Solution()
root = t.nthSuperUglyNumber(12, [2,7,13,19])

print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
