import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import itertools
import heapq
from collections import Counter

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        cx1 = max(ax1, bx1)
        cy1 = max(ay1, by1)
        cx2 = min(ax2, bx2)
        cy2 = min(ay2, by2)

        intersect = (cx2 - cx1)*(cy2 - cy1) if cy2>cy1 and cx2>cx1 else 0 
        return (ax2 - ax1)*(ay2 - ay1) + (bx2 - bx1)*(by2 - by1) - intersect
start_time = time.time()
t = Solution()
root = t.computeArea(-3, 0, 3, 4, -100, -1, -91, 2)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''