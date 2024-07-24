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
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        decrease_set = set()
        mask = 0
        result = 0
        n = len(nums)
        for i in range(len(nums)):
            if i in decrease_set:
                mask ^= 1
            nums[i] ^= mask
            if nums[i] == 0:
                if i <= n-k:
                    mask ^= 1
                    result += 1
                    decrease_set.add(i+k)
                else:
                    return -1
        return result 

start_time = time.time()
t = Solution()
root = t.minKBitFlips([1,1,0], 2)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
