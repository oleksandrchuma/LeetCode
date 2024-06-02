from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for num in nums:
            k = k^num
        return bin(k).count('1')
start_time = time.time()
app = Solution()
root = app.minOperations([2,1,3,4], 1)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


