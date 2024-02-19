import time
from typing import List
from functools import lru_cache

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and len([c for c in bin(n) if c == '1']) == 1
        
app = Solution()
start_time = time.time()
root = app.isPowerOfTwo(2)
#root = app.mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

