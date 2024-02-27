from typing import List
from typing import Optional
import time
import math
from functools import lru_cache 
from collections import Counter

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]
        if sum(diff) < 0:
            return -1
        min, pos = math.inf, 0
        x = 0
        for i in range(n+1):
            x += diff[i%n]
            if x <= min: 
                min, pos = x, i
        
        return (pos + 1) % n
start_time = time.time()
app = Solution()   
root = app.canCompleteCircuit([2, 0, 0, 0], [0,1,0,0])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
