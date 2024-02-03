from typing import List
from typing import Optional
import time
import math
import numpy
from collections import Counter
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        result = [0 for _ in arr]
        for i in range(min(k, len(arr))):
            result[i] = (i+1) * max(arr[:i+1])
        if (len(arr) > k):
            for i in range(k, len(arr)):
                result[i] = max([result[i-j] + j*max(arr[i-j+1:i+1]) for j in range(1, k+1)])    
        return result[-1]                         
start_time = time.time()
app = Solution()

root = app.maxSumAfterPartitioning([1], 1)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
