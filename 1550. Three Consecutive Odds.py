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
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        result = []
        for num in nums2:
            if num in c and c[num] > 0:
                result.append(num)
                c[num] -= 1
        return result 
start_time = time.time()
t = Solution()
root = t.intersect([1,2,2,1], [2,2])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
