from typing import List
from typing import Optional
import time
import math
from collections import Counter
from functools import lru_cache

class Solution:
    def numSquares(self, n: int) -> int:
        @lru_cache(None)
        def numSquaresRec(num):
            res = num
            for x in squares: 
                if x <= num:
                    k = numSquaresRec(num - x)
                    if (res > k + 1):
                        res = k + 1
            return res
        squares = []
        x = 1 
        while (x*x <= n):
            squares.append(x*x)
            x += 1
        
        return numSquaresRec(n)
start_time = time.time()
app = Solution()
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

