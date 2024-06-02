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
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]
start_time = time.time()
t = Solution()
val = ['a', 'b', 'c']
root = t.reverseString(val)
print(val)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
