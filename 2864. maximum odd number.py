import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import heapq
from collections import Counter

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        d = Counter(s)        
        return '1'*(d['1']-1) + '0'*d['0'] + '1'

start_time = time.time()
app = Solution()
root = app.maximumOddBinaryNumber('101001')
#root = app.calculateMinimumHP([[0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

