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
    def makeGood(self, s: str) -> str:
        result = []
        for c in s: 
            if result and c.lower() == result[-1].lower() \
                      and c != result[-1]:
                result.pop()
            else:
                result.append(c)
        return ''.join(result)
start_time = time.time()
t = Solution()
root = t.makeGood("leEeetcode")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
