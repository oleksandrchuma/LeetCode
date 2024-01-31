from typing import List
from typing import Optional
import time
import math
import numpy
from collections import Counter

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in temperatures]
        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and t > stack[-1][0]:
                _, pi = stack.pop()
                result[pi] = i - pi    
            stack.append((t, i))
        return result
start_time = time.time()
app = Solution()
root = app.dailyTemperatures([73,74,75,71,69,72,76,73])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
