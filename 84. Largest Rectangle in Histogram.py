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
    
start_time = time.time()
print(Solution().largestRectangleArea([2,1,5,6,2,3]))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
