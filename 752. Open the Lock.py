from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = [-1 for _ in range(10000)]
        for deadend in deadends:
            visited[int(deadend)] = -2
        if visited[0] == -2:
            return 0 if int(target) == 0 else -1
        if int(target) == 0:
            return 0
        visited[0] = 0
        queue = []
        queue.append(([0,0,0,0], 0))
        t = int(target)
        dir = [-1,1]
        while queue:
            v1, dist = queue.pop(0)
            dist+=1
            for i in range(4): 
                for delta in dir:
                    v2 = list(v1)
                    v2[i] = (v2[i] + delta+10)%10
                    key = 1000*v2[0]+100*v2[1]+10*v2[2]+v2[3]
                    
                    if visited[key] == -1:
                        visited[key] = dist
                        queue.append((v2, dist))
                    if key == t:
                        return dist
        return -1
start_time = time.time()
app = Solution()
root = app.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


