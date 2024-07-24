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
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        res = []
        for num in arr2:
            if num in c:
                res += [num]*c[num]
                del c[num]
        for num in sorted(c.keys()):
            res += [num]*c[num]
        return res
start_time = time.time()
t = Solution()
root = t.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
