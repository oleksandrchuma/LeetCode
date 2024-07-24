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
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        c = Counter(hand)
        keys = sorted(list(c.keys()))
        i = 0
        res = 0 
        while i+groupSize <= len(keys):
            if (keys[i]+groupSize-1 == keys[i+groupSize-1]):
                delta = min(c[k] for k in keys[i:i+groupSize])
                res += delta
                for j in range(i, i+groupSize):
                    c[keys[j]] -= delta
                    if c[keys[j]] == 0:
                        i = j
                i += 1 
            else: 
                i+=1
        return res*groupSize == len(hand)
start_time = time.time()
t = Solution()
root = t.isNStraightHand([1,2,3,6,2,3,4,7,8], 3)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
