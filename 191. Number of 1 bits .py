import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import heapq
from collections import Counter

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0 
        while n > 0:
            res += n%2
            n >>= 1
        return res 
    
start_time = time.time()
app = Solution()
root = app.hammingWeight(43261596)
#root = app.calculateMinimumHP([[0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

