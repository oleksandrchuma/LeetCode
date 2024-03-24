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
# Definition for a binary tree node.
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        intervals = []
        a = nums[0]
        delta = 0
        for i in range(1, len(nums)):
            if a + delta + 1 == nums[i]:
                delta += 1 
            else: 
                intervals.append((a, a+delta))
                a = nums[i]
                delta = 0
        intervals.append((a, a+delta))
        return [str(intv[0]) if intv[0] == intv[1] else f"{intv[0]}->{intv[1]}" for intv in intervals]
start_time = time.time()
t = Solution()
root = t.summaryRanges([0,1,2,4,5,7])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''