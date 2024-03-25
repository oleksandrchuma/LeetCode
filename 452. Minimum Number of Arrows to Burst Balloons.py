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
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return len(points)
        points.sort(key=lambda item: item[0])
        i = 1
        current = points[0]
        result = 1
        while i < len(points):
            if current[1] < points[i][0]:
                result += 1
                current = points[i]
            else: 
                current = [points[i][0], min(points[i][1], current[1])]
            i += 1
        
        return result
    
start_time = time.time()
t = Solution()
root = t.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''