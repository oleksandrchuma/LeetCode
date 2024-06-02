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
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = [0 for _ in range(nums[-1]+1)]
        count = 0
        def rec(i):
            nonlocal count
            if i == len(nums):
                return
            if (nums[i]-k<=0 or  cnt[nums[i]-k]== 0):
                cnt[nums[i]]+=1
                count += 1
                rec(i+1)
                cnt[nums[i]]-=1
            rec(i+1)
        rec(0)
        return count
                            
start_time = time.time()
t = Solution()
root = t.beautifulSubsets([1,1,2,3], 1)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
