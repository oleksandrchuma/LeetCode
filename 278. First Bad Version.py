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

def isBadVersion(version: int) -> bool:
    return version > 2
def check(idx: int):
    return isBadVersion(idx+1) and (idx == 0 or not(isBadVersion(idx)))
class Solution:
    def firstBadVersion(self, n: int) -> int:        
        left, right = 0, n-1
        while left < right:
            mid = (left+right)//2
            if check(mid):
                return mid+1
            if isBadVersion(mid+1):
                right = mid-1
            else:
                left = mid+1
        return left+1
start_time = time.time()
t = Solution()
root = t.firstBadVersion(10)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
