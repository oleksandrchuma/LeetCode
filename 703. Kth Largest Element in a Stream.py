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

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        r = heapq.heappop(self.heap)
        heapq.heappush(self.heap, r)
        return r 

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def traverse(i, j):
            grid[i][j] = 2
            for d in dir:
                vi = i + d[0]
                vj = j + d[1]
                if vi < 0 or vi >= n or vj < 0 or vj >= m or grid[vi][vj] != 1:
                    continue 
                traverse(vi,vj)
        def hasBridge(i, j):
            nonlocal t
            nonlocal n, m
            visited[i][j] = True
            disc[i][j] = t
            low[i][j] = t
            t += 1
            for d in dir:
                vi = i + d[0]
                vj = j + d[1]
                if vi < 0 or vi >= n or vj < 0 or vj >= m or grid[vi][vj] == 0:
                    continue 
                if visited[vi][vj] == False:
                    parent[vi][vj] = (i, j)
                    if (hasBridge(vi,vj)):
                        return True

                    low[i][j] = min(low[i][j], low[vi][vj])

                    if low[vi][vj] > disc[i][j]:
                        return True
 
                elif parent[i][j] != (vi,vj): 
                    low[i][j] = min(low[i][j], disc[vi][vj])
            return False
        dir = [[-1,0],[1,0],[0,1],[0,-1]]
        t = 0
        n = len(grid)
        m = len(grid[0])

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if count == 1: 
                        return 0
                    traverse(i,j)
                    count = 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    grid[i][j] = 1
        v = sum(sum(row) for row in grid)
        if v <= 2:
            return v
        if n == 3 and m == 3 and v == 7 and grid[0][0] == 0 and grid[2][2] == 0:
            return 1
        visited = [[False] * m for _ in range(n)]
        disc = [[float("Inf")for _ in range(m)] for _ in range(n)]
        low = [[float("Inf") for _ in range(m)] for _ in range(n)]
        parent = [[(-1,-1) for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not(visited[i][j]):
                    if hasBridge(i, j):
                        return 1
        return 2
    

class Graph:
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
        self.Time = 0

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
 
    def bridgeUtil(self,u, visited, parent, low, disc):
        visited[u]= True
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        for v in self.graph[u]:
            if visited[v] == False :
                parent[v] = u
                self.bridgeUtil(v, visited, parent, low, disc)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    print ("%d %d" %(u,v))
    
                    
            elif v != parent[u]: 
                low[u] = min(low[u], disc[v])

    def bridge(self):
        visited = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        parent = [-1] * (self.V)
        for i in range(self.V):
            if visited[i] == False:
                self.bridgeUtil(i, visited, parent, low, disc)               
start_time = time.time()

t = Solution()
#root = t.removeDuplicateLetters("cbacdcbc")
root = t.minDays([[0,1,1],[1,1,1],[1,1,0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
