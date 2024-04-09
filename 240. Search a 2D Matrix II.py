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
    def search(self, matrix, target, x1, y1, x2, y2):
        if x1 > x2 or y1 > y2: 
            return False
        if x1 == x2 and y1 == y2: 
            return matrix[y1][x1] == target
        left = 0 
        ky, kx = 1, 1
        if x1 == x2: 
            right = y2 - y1 
            kx = 0
        elif y1 == y2:
            right = x2 - x1 
            ky = 0
        else:
            right = min(x2 - x1, y2 - y1)
        while left < right:
            mid = (right + left)//2
            midval = matrix[y1+mid*ky][x1+mid*kx]    
            if midval == target: 
                return True
            if midval < target:
                left = mid+1
            else:
                right = mid-1    
        leftval = matrix[y1+left*ky][x1+left*kx]
        if leftval == target:
            return True 
        if kx == 0 or ky == 0:
            return False        
        if leftval > target:
            left -= 1
        if left < 0: 
            return False 
        return self.search(matrix, target, x1+left+1, y1, x2, y1+left)\
                or self.search(matrix, target, x1, y1+left+1, x1+left, y2)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        return self.search(matrix, target, 0, 0, m-1, n-1)
start_time = time.time()
t = Solution()

root = t.searchMatrix([[1,1]], 2)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
