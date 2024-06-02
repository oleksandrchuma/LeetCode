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
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        right = 0
        res = 0
        n = len(s)
        while right < n and left < n:
            while right < n and abs(ord(s[right])-ord(t[right]))<=maxCost: 
                maxCost -= abs(ord(s[right])-ord(t[right]))
                right += 1
            if right - left > res:
                res = right - left
            maxCost +=  abs(ord(s[left])-ord(t[left]))
            left += 1
        return res
start_time = time.time()
t = Solution()
root = t.equalSubstring("abcd", "bcdf", 3)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
