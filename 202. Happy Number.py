import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import heapq
from collections import Counter

class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n not in s:
            s.add(n)
            n = sum([int(c)*int(c) for c in str(n)])
        return n == 1

start_time = time.time()
app = Solution()
root = app.isHappy(2)

#root = app.calculateMinimumHP([[0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

