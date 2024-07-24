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
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def getResult(vertex: int):
            if vertex in result:
                return result[vertex]
            ancestors = set()
            for parent in parents[vertex]:
                ancestors.add(parent)
                ancestors = ancestors | getResult(parent)
            result[vertex] = ancestors
            return ancestors
        parents = [set() for _ in range(n)]
        for edge in edges:
            parents[edge[1]].add(edge[0])
        result = defaultdict(set)
        return [sorted(list(getResult(i))) for i in range(n)]
start_time = time.time()
t = Solution()
root = t.getAncestors(8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
