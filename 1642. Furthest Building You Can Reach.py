from typing import List
from typing import Optional
import bisect
import time
import heapq
from collections import Counter

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if len(heights) <= 1:
            return 0
        used = []
        result = len(heights)-1
        
        for i in range(1, len(heights)):
            h = heights[i] - heights[i-1]    
            if h <= 0:
                continue
            if ladders > 0:
                ladders -= 1
                heapq.heappush(used, h)
                continue
            if len(used) > 0 and used[0] < h:
                prev = heapq.heappop(used)
                bricks += h - prev
                heapq.heappush(used, h)
            if bricks >= h:
                bricks -= h
            else:
                result = i - 1
                break
        return result
    
start_time = time.time()
app = Solution()   

root = app.furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
