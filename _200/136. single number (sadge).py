from typing import List
from typing import Optional
import time
import math
from functools import lru_cache 
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result 
start_time = time.time()
app = Solution()   
root = app.singleNumber([1,2,2,3,3])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")