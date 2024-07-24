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
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [x[1] for x in sorted(zip(heights, names), reverse=True)]
start_time = time.time()
t = Solution()
#[5,1,2,3,null,6,4]
root = t.sortPeople(["Mary","John","Emma"], [180,165,170])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
