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
    def maximalRectangleSlow(self, matrix: List[List[str]]) -> int:
        if (len(matrix) == 0):
            return 0
        n = len(matrix)
        m = len(matrix[0])
        max_val = 0
        res = [[set() for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    if j > 0 and i > 0:
                        res[i][j].update(res[i-1][j].intersection(res[i][j-1]))
                    if j > 0:
                        res[i][j].update(x for x in res[i][j-1] if x[0]==i)
                    if i > 0:
                        res[i][j].update(x for x in res[i-1][j] if x[1]==j)
                    res[i][j].add((i,j))
                    max_val = max(max([(i-p[0]+1)*(j-p[1]+1) for p in res[i][j] if p[0]==p[1]], default=1), max_val)
        '''for m in matrix:
            print(m)
        for r in res:
            print(r)'''
        return max_val
    
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if (len(matrix) == 0):
            return 0
        n = len(matrix)
        m = len(matrix[0])
        max_val = 0
        res = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    if j > 0 and i > 0:
                        res[i][j] = min(res[i-1][j-1], res[i-1][j], res[i][j-1]) +1
                    else: 
                        res[i][j] = 1
        max_val = max([res[i][j] for i in range(n) for j in range(m)])
        return max_val*max_val
start_time = time.time()
t = Solution()
root = t.maximalSquare([["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''