import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import heapq 
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            columnNumber -= 1
            res = chr(ord("A")+(columnNumber%26)) + res
            columnNumber //= 26
        return res
app = Solution()
start_time = time.time()
root = app.convertToTitle(1)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

