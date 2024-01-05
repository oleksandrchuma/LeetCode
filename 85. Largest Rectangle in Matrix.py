from typing import List
from typing import Optional
import time
import math
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        max = 0
        for i in range(len(heights)):
            k = i
            while len(stack) > 0 and stack[-1][0] > heights[i]:
                (h, index) = stack.pop()
                max = h * (i - index) if h * (i - index) > max else max 
                k = index
            stack.append((heights[i], k))        
        return max
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        result = 0
        intervals = [0] * len(matrix[0])
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    intervals[col] += 1
                else: 
                    intervals[col] = 0
            maxd = self.largestRectangleArea(intervals)              
            if (maxd > result):
                result = maxd
        return result
    
start_time = time.time()
print(Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
