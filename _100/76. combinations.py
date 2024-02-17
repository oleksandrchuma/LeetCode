from typing import List
from typing import Optional
import time
from collections import Counter
import math
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        rez = []
        v = []
        stack = []
        stack.append(v)
        while (len(stack)):
            v = stack.pop(0)
            for i in range(0 if len(v) == 0 else v[-1], n - k + 1 + len(v)):
                x = v + [i+1] 
                if (len(x) == k):
                    rez.append(x)
                else:
                    stack.append(x)

        return rez 
start_time = time.time()
print(Solution().combine(4, 2))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

