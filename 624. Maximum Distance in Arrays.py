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
import pprint

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mins = sorted([(min(a), i) for i, a in enumerate(arrays)])
        maxs = sorted([(max(a), i) for i, a in enumerate(arrays)], reverse=True)
        print(mins, maxs)
        if mins[0][1] != maxs[0][1]:
            return maxs[0][0] - mins[0][0]        
        else:
            return max(maxs[1][0] - mins[0][0], maxs[0][0] - mins[1][0])
             
start_time = time.time()

t = Solution()
#root = t.removeDuplicateLetters("cbacdcbc")
root = t.maxDistance([[1,2,3],[4,5],[1,2,3]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
