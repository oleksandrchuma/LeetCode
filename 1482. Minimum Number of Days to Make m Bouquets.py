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
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def calc(h) -> int:
            result = 0
            j = -1
            for i in range(n):
                if bloomDay[i] > h:
                    result += (i-j-1)//k
                    j = i
            result += (n-j-1)//k    
            return result 
        n = len(bloomDay)
        if (m*k) > n: 
            return -1
        right = max(bloomDay)
        left = 0
        while left < right: 
            mid = (left+right)//2
            mid_val = calc(mid)
            if mid_val < m: 
                left = mid+1
            else: 
                right = mid-1
        left_val = calc(left)
        if left_val < m:
            left+=1
        return left
start_time = time.time()
t = Solution()
root = t.minDays([1,10,3,10,2], 3, 1)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
