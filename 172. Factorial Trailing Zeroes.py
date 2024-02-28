import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import heapq 

class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n >= 5:
            res += n//5 
            n //= 5
        return res    
    
app = Solution()
start_time = time.time()
root = app.trailingZeroes(100)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

