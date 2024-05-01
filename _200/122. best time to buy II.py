from typing import List
from typing import Optional
import time
import math
from collections import Counter

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]

        return res
  
start_time = time.time()
app = Solution()
print(app.maxProfit([7,1,5,3,6,4]))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

