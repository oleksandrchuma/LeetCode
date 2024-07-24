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
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        result = 2*sum([c//2 for c in c.values()])
        if result < len(s):
            result += 1
        return result 
start_time = time.time()
t = Solution()
root = t.longestPalindrome("abccccdd")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
