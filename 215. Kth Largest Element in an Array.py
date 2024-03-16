import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import itertools
import heapq
from collections import Counter

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for num in nums:
            if len(res) == k:
                low = heapq.heappop(res)
                heapq.heappush(res, max(low, num))
            else:
                heapq.heappush(res, num)
        return heapq.heappop(res) if len(res) == k else -1
start_time = time.time()
t = Solution()
root = t.findKthLargest([3,2,1,5,6,4], 2)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''