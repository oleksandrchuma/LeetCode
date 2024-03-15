import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import heapq
from collections import Counter

class Solution:
    def countPrimes(self, n: int)->int:
        primes = [1 for _ in range(n)]
        m = min(n//2, int(math.sqrt(n)))
        for i in range(2, m+1):
            if primes[i] == 1:
                k = i*2
                while k < n:
                    primes[k] = 0
                    k += i
        return len([p for i,p in enumerate(primes) if p == 1 and i>1]) 
start_time = time.time()
app = Solution()
root = app.countPrimes(5)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

