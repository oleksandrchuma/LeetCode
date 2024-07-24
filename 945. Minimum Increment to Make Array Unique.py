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
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        high = nums[0]
        result = 0
        for i in range(1, len(nums)):
            high += 1
            if nums[i] >= high: 
                high = nums[i]
            else:
                result += high-nums[i]
        return result 
start_time = time.time()
t = Solution()
root = t.minIncrementForUnique([3,2,1,2,1,7])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
