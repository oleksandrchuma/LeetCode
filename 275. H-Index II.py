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
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def check(idx):
            return citations[idx] >= len(citations)-idx \
                and (idx == 0 or citations[idx-1] < len(citations)-idx+1)
        print(citations)
        left = 0 
        right = len(citations)-1
        while left < right:
            mid = (left+right)//2
            if check(mid):
                return len(citations)-mid
            if citations[mid] < len(citations)-mid:
                left = mid+1
            else: 
                right = mid-1
        return len(citations)-left if check(left) else 0
start_time = time.time()
t = Solution()
root = t.hIndex([0])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
