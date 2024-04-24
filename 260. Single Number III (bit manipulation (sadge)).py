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
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = 0 
        for num in nums:
            s = s^num
        i = 0
        while s % 2 == 0:
            i += 1
            s = s>>1
        x1= 0
        x2 = 0
        for num in nums:
            if (num>>i)%2 == 0:
                x1 = x1^num 
            else: 
                x2 = x2^num
        return [x1,x2] 
start_time = time.time()
t = Solution()
root = t.singleNumber([1,2,1,3,2,5])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
