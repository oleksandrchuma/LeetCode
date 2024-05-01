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
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        step = [(0,0)]
        n = len(ring)
        for i in range(len(key)):
            next = []
            for j in range(len(ring)):
                if key[i] == ring[j]:
                    weights = []
                    for pos, weight in step:
                        weights.append(weight + min(abs(j-pos), n-abs(j-pos)))
                    next.append((j, min(weights)))
            step = next
        return min(weight for _, weight in step)+len(key)
start_time = time.time()
t = Solution()
root = t.findRotateSteps("godding", "godding")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
