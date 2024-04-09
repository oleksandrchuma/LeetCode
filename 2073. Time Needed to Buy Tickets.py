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
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0
        for i in range(len(tickets)):
            result += min(tickets[i], tickets[k]) if i <= k else min(tickets[i], tickets[k]-1) 
        return result 
start_time = time.time()
t = Solution()

root = t.timeRequiredToBuy([5,1,1,1], 0)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
