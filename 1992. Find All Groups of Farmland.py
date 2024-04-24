import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
from queue import Queue
import math
import itertools
import heapq
from collections import Counter
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic = defaultdict(list)
        for edge in edges: 
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])
        visited = {source}
        queue = [source]
        while queue:
            v1 = queue.pop(0)
            if v1 == destination:
                break
            for v2 in dic[v1]:
                if v2 not in visited:
                    visited.add(v2)
                    queue.append(v2)
                    
        return destination in visited


start_time = time.time()
t = Solution()
root = t.validPath(3, [[0,1],[1,2],[2,0]], 0, 2)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
