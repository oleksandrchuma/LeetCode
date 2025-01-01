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
import pprint

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        result = defaultdict(list) 
        adjusted = [[] for _ in range(n)]
        visited = [0]*n
        current = {}
        current[0] = [0]
        for edge in edges:
            adjusted[edge[0]-1].append(edge[1]-1)
            adjusted[edge[1]-1].append(edge[0]-1)
        appended = set()
        stack = []
        stack.append((0,0))
        while stack:
            v,l = stack.pop(0)
            if visited[v] == 2:
                continue
            if visited[v]==1 and result[v][0] == l:
                continue
            visited[v] += 1
            result[v].append(l)
            if v == n-1 and visited[v] == 2:
                break
            for v2 in adjusted[v]:
                if (v2,l+1) not in appended:
                    stack.append((v2,l+1))
                    appended.add((v2,l+1))
        t = 0
        k = result[n-1][1]
        print(k)
        for i in range(k-1):
            t += time
            tick = t//change
            if tick%2 == 1:
                t = (tick+1)*change                 
        return t+time
                            
start_time = time.time()
t = Solution()
#root = t.removeDuplicateLetters("cbacdcbc")
root = t.secondMinimum(5, [[1,2],[1,3],[1,4],[3,4],[4,5]], 3, 5)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
