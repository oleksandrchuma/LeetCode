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
class DisjointSet: 
    def __init__(self, size): 
        self.parent = [i for i in range(size)] 
        self.rank = [0] * size 

    # Function to find the representative (or the root node) of a set 
    def find(self, i): 
        # If i is not the representative of its set, recursively find the representative 
        if self.parent[i] != i: 
            self.parent[i] = self.find(self.parent[i])  # Path compression 
        return self.parent[i] 

    # Unites the set that includes i and the set that includes j by rank 
    def union_by_rank(self, i, j): 
        # Find the representatives (or the root nodes) for the set that includes i and j 
        irep = self.find(i) 
        jrep = self.find(j) 

        # Elements are in the same set, no need to unite anything 
        if irep == jrep: 
            return

        # Get the rank of i's tree 
        irank = self.rank[irep] 

        # Get the rank of j's tree 
        jrank = self.rank[jrep] 

        # If i's rank is less than j's rank 
        if irank < jrank: 
            # Move i under j 
            self.parent[irep] = jrep 
        # Else if j's rank is less than i's rank 
        elif jrank < irank: 
            # Move j under i 
            self.parent[jrep] = irep 
        # Else if their ranks are the same 
        else: 
            # Move i under j (doesn't matter which one goes where) 
            self.parent[irep] = jrep 
            # Increment the result tree's rank by 1 
            self.rank[jrep] += 1
class Solution:    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic = DisjointSet(n)
        for edge in edges: 
            dic.union_by_rank(edge[0], edge[1])            
        return dic.find(destination) == dic.find(source)
    
start_time = time.time()
t = Solution()
root = t.validPath(3, [[0,1],[1,2],[2,0]], 0, 2)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
