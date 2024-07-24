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
# Definition for singly-linked list.

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        res = []
        stack = []
        robots = sorted([(p,h,d,o) for p,h,d,o in zip(positions, healths, directions, range(len(positions)))])
        for p,h,d,o in robots:
            if d == 'R':
                stack.append((h,o))
            elif d == 'L':
                while stack and h > 0:
                    lh,lo = stack.pop()
                    if lh == h:
                        h = 0
                        break
                    if lh > h:
                        if lh > 1:
                            stack.append((lh-1, lo))
                        h = 0
                        break
                    
                    h -= 1
                if h > 0:
                    res.append((o,h))
        while stack:
            h,o = stack.pop()
            res.append((o,h))
        res.sort()
        return [h for _,h in res] 
start_time = time.time()
t = Solution()
root = t.survivedRobotsHealths([4,47], [15,24], "RR")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
