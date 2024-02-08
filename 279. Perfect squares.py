from typing import List
from typing import Optional
import time
import math
from collections import Counter
from functools import lru_cache

class Solution:
    def numSquares2(self, n: int) -> int:
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

    def numSquares(self, n: int) -> int:
        squares = []
        x = 2 
        while (x*x <= n):
            squares.append(x*x)
            x += 1
        res = [i for i in range(0, n+1)]
        for i in range(2, n+1):
            for k in squares:
                if k > i:
                    break
                if res[i-k] + 1 < res[i]:
                    res[i] = res[i-k] + 1
        return res[-1]
start_time = time.time()
app = Solution()
print(app.numSquares(13))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

