from typing import List
from typing import Optional
import time
import math
from collections import Counter

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        low = prices[0]
        high = prices[0]
        delta = 0
        for i in range(1, len(prices)):
            if prices[i] < low:
                delta = max(delta, high - low)
                high = low = prices[i]
            if prices[i] > high: 
                high = prices[i]  
                
        delta = max(delta, high - low)
        return delta
  
start_time = time.time()
app = Solution()
print(app.maxProfit([2,4,1]))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

