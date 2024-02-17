from typing import List
from typing import Optional
import time
import math
from collections import Counter

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0] * pow(2, n)
        result[1] = 1
        base = 2 
        for _ in range(n-1):
            next = base * 2
            for i in range(base):
                result[next - i - 1] = result[i] + base
            base = next
        return result 

start_time = time.time()
print(Solution().grayCode(3))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

