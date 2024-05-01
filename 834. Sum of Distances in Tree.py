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
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        def buildTree(node):
            if len(children[node]) == 0:
                leaveCount[node] = 1
                return 0 
            weight = 0
            for child in children[node]:
                children[child].remove(node)
                weight += buildTree(child)
                leaveCount[node] += leaveCount[child]
            weight += leaveCount[node]
            leaveCount[node] += 1
            sums[node] = weight 
            return weight  
        def fillResult(node, upstream, value):
            total = upstream + leaveCount[node]
            for child in children[node]:
                result[child] = value + total - 2*leaveCount[child]
                fillResult(child, total - leaveCount[child], result[child])
        sums = [0]*n
        result = [0]*n
        leaveCount = [0]*n
        children = defaultdict(list)
        for edge in edges:
            children[edge[0]].append(edge[1])
            children[edge[1]].append(edge[0])
        result[0] = buildTree(0)
        fillResult(0, 0, result[0])
        return result

start_time = time.time()
t = Solution()
#root = t.sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]])
root = t.sumOfDistancesInTree(2, [[0,1]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
