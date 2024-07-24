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
import numpy 
import pprint

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def bfs(type: int) -> bool:
            stack=[0]
            visited=set()
            visited.add(0)
            while stack:
                tree = stack.pop()
                for node in forest[tree]:
                    for sibling in v[type][node]:
                        if v_forest[sibling] not in visited:
                            stack.append(v_forest[sibling])
                            visited.add(v_forest[sibling])
            return len(visited) == len(forest)
        v = [[[] for _ in range(n)] for _ in range(3)]
        edge_by_type = [0]*3

        for edge in edges:
            v[edge[0]-1][edge[1]-1].append(edge[2]-1)
            v[edge[0]-1][edge[2]-1].append(edge[1]-1)
            edge_by_type[edge[0]-1] += 1
        forest = []
        spare = 0
        v_forest = [-1]*n
        for i in range(n):
            if v_forest[i] == -1:
                tree = set()
                tree.add(i)
                stack = [i]
                tree_index = len(forest)
                v_forest[i] = tree_index
                while stack:
                    node = stack.pop()
                    for child in v[2][node]:
                        if child not in tree: 
                            stack.append(child)
                            tree.add(child)
                            v_forest[child] = tree_index
                forest.append(list(tree))
        
        #print(v)
        #print(edge_by_type)
        #print(forest)
        #print(v_forest)
        #print(spare)
        if not(bfs(0)) or not(bfs(1)):
            return -1

        return edge_by_type[2]-n+len(forest) + (edge_by_type[0]-len(forest)+1) + (edge_by_type[1]-len(forest)+1)
start_time = time.time()
t = Solution()
root = t.maxNumEdgesToRemove(13, [[1,1,2],[2,1,3],[3,2,4],[3,2,5],[1,2,6],[3,6,7],[3,7,8],[3,6,9],[3,4,10],[2,3,11],[1,5,12],[3,3,13],[2,1,10],[2,6,11],[3,5,13],[1,9,12],[1,6,8],[3,6,13],[2,1,4],[1,1,13],[2,9,10],[2,1,6],[2,10,13],[2,2,9],[3,4,12],[2,4,7],[1,1,10],[1,3,7],[1,7,11],[3,3,12],[2,4,8],[3,8,9],[1,9,13],[2,4,10],[1,6,9],[3,10,13],[1,7,10],[1,1,11],[2,4,9],[3,5,11],[3,2,6],[2,1,5],[2,5,11],[2,1,7],[2,3,8],[2,8,9],[3,4,13],[3,3,8],[3,3,11],[2,9,11],[3,1,8],[2,1,8],[3,8,13],[2,10,11],[3,1,5],[1,10,11],[1,7,12],[2,3,5],[3,1,13],[2,4,11],[2,3,9],[2,6,9],[2,1,13],[3,1,12],[2,7,8],[2,5,6],[3,1,9],[1,5,10],[3,2,13],[2,3,6],[2,2,10],[3,4,11],[1,4,13],[3,5,10],[1,4,10],[1,1,8],[3,3,4],[2,4,6],[2,7,11],[2,7,10],[2,3,12],[3,7,11],[3,9,10],[2,11,13],[1,1,12],[2,10,12],[1,7,13],[1,4,11],[2,4,5],[1,3,10],[2,12,13],[3,3,10],[1,6,12],[3,6,10],[1,3,4],[2,7,9],[1,3,11],[2,2,8],[1,2,8],[1,11,13],[1,2,13],[2,2,6],[1,4,6],[1,6,11],[3,1,2],[1,1,3],[2,11,12],[3,2,11],[1,9,10],[2,6,12],[3,1,7],[1,4,9],[1,10,12],[2,6,13],[2,2,12],[2,1,11],[2,5,9],[1,3,8],[1,7,8],[1,2,12],[1,5,11],[2,7,12],[3,1,11],[3,9,12],[3,2,9],[3,10,11]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
