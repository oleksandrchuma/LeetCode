from typing import List
from typing import Optional
import time
import math
from collections import Counter
from functools import lru_cache
from fractions import Fraction

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return len(points)
        lines = [[(math.inf,math.inf,math.inf) for _ in points] for _ in points]
        for i1 in range(len(points)):
            for i2 in range(i1):
                lines[i1][i2] = self.getLine(points[i1], points[i2])
        res = 2
        for lineRow in lines:
            counter = Counter([line for line in lineRow if line[0] != math.inf or line[1] != math.inf or line[2] != math.inf])
            if (len(counter) > 0):
                res = max(max(counter.values())+1, res)
        print(lines)
        return res
    def getLine(self, p1, p2):        
        kx = p2[1]-p1[1]
        ky = p1[0]-p2[0]
        c = p1[0]*(p1[1]-p2[1])+p1[1]*(p2[0]-p1[0])
        if c != 0: 
            return (Fraction(kx, c), Fraction(ky, c), 1)
        elif ky != 0: 
            return (Fraction(kx, ky), 1, 0)
        else: 
            return (0, 0, 0)

start_time = time.time()
app = Solution()
data = [1,1]
root = app.maxPoints([[0,1],[0,0],[0,4],[0,-2],[0,-1],[0,3],[0,-4]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

