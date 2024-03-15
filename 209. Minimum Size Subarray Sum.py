import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import heapq
from collections import Counter

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start,end,total = -1,-1,0
        n = len(nums)
        res = len(nums)+1 
        while end < n-1:
            while total < target and end < n-1:
                end += 1 
                total += nums[end]
            if total < target:
                break
            while total >= target and start <= end:
                total -= nums[start] if start >= 0 else 0
                start += 1
            if total < target:
                res = min(res, end-start+2)
            else:
                res = 1
                break
        return res if res <= len(nums) else 0
start_time = time.time()
app = Solution()
root = app.minSubArrayLen(7, [8])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

