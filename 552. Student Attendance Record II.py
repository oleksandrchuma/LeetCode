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
    def checkRecord(self, n: int) -> int:
        p = [0 for _ in range(n+1)]
        a = [0 for _ in range(n+1)]
        p[0] = 1
        for i in range(1,n+1):
            p[i] = p[i-1]
            a[i] = a[i-1]+p[i-1]
            if i > 1:
                p[i] += p[i-2]
                a[i] += a[i-2]+p[i-2]
            if i > 2:
                p[i] += p[i-3]
                a[i] += a[i-3]+p[i-3]
        
        return (p[n]+p[n-1]+(p[n-2] if n > 1 else 0)\
                + a[n]+a[n-1]+(a[n-2] if n > 1 else 0))%(pow(10,9) + 7)
start_time = time.time()
t = Solution()
root = t.checkRecord(10101)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
