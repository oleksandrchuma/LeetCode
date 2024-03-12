import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import heapq
from collections import Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))        
start_time = time.time()
t = Solution()
root = t.intersection([4,9,5], [9,4,9,8,4])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

