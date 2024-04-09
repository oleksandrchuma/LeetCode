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
    def checkValidString(self, s: str) -> bool:
        bottom = 0 
        top = 0
        for c in s: 
            if c == '(':
                bottom += 1
                top += 1
            elif c == ')':
                if bottom > 0:
                    bottom -= 1
                top -= 1
                if top < 0:
                    return False
            elif c == '*':
                top += 1
                if bottom > 0:
                    bottom -= 1
        return bottom == 0
start_time = time.time()
t = Solution()

root = t.checkValidString("((((*))")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
