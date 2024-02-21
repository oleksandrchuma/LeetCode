import time
from typing import List
from functools import lru_cache

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        pow2 = 1
        while (pow2*2 <= right):
            pow2*=2
        result = 0
        while pow2 >= 1 and left > 0 and right > 0:
            if left >= pow2 and right >= pow2:
                result += pow2
                left -= pow2
                right -= pow2
            elif right >= pow2:
                break
            pow2 //= 2
        return result 
app = Solution()
start_time = time.time()
root = app.rangeBitwiseAnd(15, 15)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

