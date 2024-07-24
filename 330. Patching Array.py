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
    def minPatches(self, nums: List[int], n: int) -> int:
        s = 0
        i = 0
        result = 0
        while s < n:
            if i < len(nums) and nums[i] <= s+1:
                s += nums[i]
                i +=1
            else: 
                s += s+1
                result += 1
        return result
start_time = time.time()
t = Solution()
root = t.minPatches([1,5,10], 20)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
