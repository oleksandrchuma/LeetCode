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
    def numSteps(self, s: str) -> int:
        n = len(s)
        res = n-1
        k = len(s)-1
        while k > 0 and s[k] == '0':
            k-=1
        
        if k > 0:
            res += 2
            res += len([i for i in range(k) if s[i]=='0'])
        return res
start_time = time.time()
t = Solution()
root = t.numSteps("10")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
