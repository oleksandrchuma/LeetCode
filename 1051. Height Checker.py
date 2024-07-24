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
    def heightChecker(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        res = 0
        for i in range(len(nums)):
            if (nums[i] != nums2[i]):
                res+=1
        return res 
start_time = time.time()
t = Solution()
root = t.heightChecker([1,1,4,2,1,3])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
