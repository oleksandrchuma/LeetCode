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
    def sortGraph(self, k: int, edges: List[List[int]]) -> List[int]:
        result = []
        adjacent = defaultdict(set)
        indegree = [0]*k
        for edge in edges:
            if edge[1]-1 not in adjacent[edge[0]-1]:
                adjacent[edge[0]-1].add(edge[1]-1)
                indegree[edge[1]-1] += 1
        q = Queue()
        for i in range(k):
            if indegree[i] == 0:
                q.put(i)
        while not(q.empty()):
            v = q.get()
            result.append(v)
            for adj in adjacent[v]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.put(adj)
            
        return result if len(result) == k else []
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_order = self.sortGraph(k, rowConditions)
        col_order = self.sortGraph(k, colConditions)
        if len(row_order) == 0 or len(col_order) == 0:
            return []
        print(row_order)
        print(col_order)
        row_dic = {item:index for index, item in enumerate(row_order)}
        col_dic = {item:index for index, item in enumerate(col_order)}
        print(row_dic)
        print(col_dic)
        result = [[0]*k for _ in range(k)]
        for i in range(k):
            result[row_dic[i]][col_dic[i]] = i+1
        return result
start_time = time.time()
t = Solution()
#[5,1,2,3,null,6,4]
root = t.buildMatrix(8, [[1,2],[7,3],[4,3],[5,8],[7,8],[8,2],[5,8],[3,2],[1,3],[7,6],[4,3],[7,4],[4,8],[7,3],[7,5]],
                      [[5,7],[2,7],[4,3],[6,7],[4,3],[2,3],[6,2]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
