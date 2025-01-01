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
import pprint
# Definition for singly-linked list.
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return len([c for c in bin(start^goal) if c == '1'])

t = Solution()
start_time = time.time()
#root = t.removeDuplicateLetters("cbacdcbc")
root = t.minBitFlips(10, 7)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
