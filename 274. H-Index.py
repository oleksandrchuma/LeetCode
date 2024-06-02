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
        citations.sort(reverse=True)
        print(citations)
        for i in range(len(citations)-1,-1,-1):
            if citations[i]>=i+1:
                return i+1
        return 0
start_time = time.time()
t = Solution()
root = t.hIndex([1,3,1])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
