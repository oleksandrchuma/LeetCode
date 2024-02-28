import time
from typing import List
from functools import lru_cache

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        v = [0 for i in range(n)]
        for t in trust:
            if (t[1] != t[0]):
                v[t[1]-1] += 1
            else:
                v[t[1]-1] -= 2
            v[t[0]-1] -= 1
        return next((i+1 for i,c in enumerate(v) if c == n-1), -1) 
app = Solution()
start_time = time.time()
root = app.findJudge(3, [[1,3],[2,3]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

