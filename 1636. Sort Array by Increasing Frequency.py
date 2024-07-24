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
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sum([[-i]*c for (c, i) in sorted((count, -item) for (item, count) in Counter(nums).items())], [])
start_time = time.time()
t = Solution()
#[5,1,2,3,null,6,4]
root = t.frequencySort([-1,1,-6,4,5,-6,1,4,1])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
