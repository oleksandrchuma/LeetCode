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
    
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(root, parent):
            path = []
            for child in children[root]:
                if child != parent:
                    child_path = dfs(child, root)
                    if len(child_path) > len(path):
                        path = child_path
            return [root] + path
        if n <= 2:
            return [_ for _ in range(n)]
        children = [[] for _ in range(n)]
        for edge in edges:
            children[edge[0]].append(edge[1])
            children[edge[1]].append(edge[0])
        p1 = dfs(0, None)
        p2 = dfs(p1[-1], None)
        if len(p2) % 2 == 1:
            return [p2[len(p2)//2]]
        return p2[len(p2)//2-1:len(p2)//2+1]
        
start_time = time.time()
t = Solution()
root = t.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
