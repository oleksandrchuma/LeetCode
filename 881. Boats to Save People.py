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
import bisect
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        people.sort(reverse=True)
        left = -1
        right = len(people)
        while left + 1 < right:
            left += 1
            res += 1
            if left + 1 < right and people[right-1]+people[left] <= limit: 
                right -= 1
            
        return res 
start_time = time.time()
t = Solution()
root = t.numRescueBoats([3,2,2,1], 3)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
