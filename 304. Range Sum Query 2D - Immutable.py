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
class NumArray:

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right+1]-self.sums[left]

    
    def __init__(self, matrix: List[List[int]]):
        self.sums = []
        for row in range(len(matrix)):
            sum_row = []
            s = 0
            for col in range(len(matrix[row])):        
                s += matrix[row][col]
                sum_row.append(s+self.sums[-1][col])
            self.sums.append(sum_row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.sums[row2][col2]
        if (col1 > 0):
            res -= self.sums[row2][col1-1]
        if (row1 > 0):
            res -= self.sums[row1-1][col2]
        if (row1 > 0 and col1 > 0):
            res += self.sums[row1-1][col1-1]
        return res 
start_time = time.time()
t = Solution()
root = t.removeInvalidParentheses("(a)())()")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
