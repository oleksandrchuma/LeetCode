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
    def isUgly(self, n: int) -> bool:
        fact = [2, 3, 5]
        for f in fact:
            while n % f == 0:
                n //= f
        return n == 1
start_time = time.time()
t = Solution()
root = t.isUgly(6)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
