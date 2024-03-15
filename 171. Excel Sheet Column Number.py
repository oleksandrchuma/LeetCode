import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import heapq 
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for c in columnTitle:
            result = 26*result + ord(c)-ord('A') + 1
        return result
app = Solution()
start_time = time.time()
root = app.titleToNumber("AA")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

