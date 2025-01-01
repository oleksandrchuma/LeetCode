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
    def removeStones(self, stones: List[List[int]]) -> int:
        visited = set()
        rows = defaultdict(list)
        cols = defaultdict(list)
        n = len(stones)
        for s in stones:
            rows[s[0]].append((s[0],s[1]))
            cols[s[1]].append((s[0],s[1]))
        heap = []
        rd = defaultdict(int)
        cd = defaultdict(int)
        for s in stones:
            heapq.heappush(heap, (len(rows[s[0]])+len(cols[s[1]])-2, (s[0],s[1])))
        result = 0
        while (heap):
            w, s = heapq.heappop(heap)
            if s in visited:
                continue
            visited.add(s)
            if len(visited) == n:
                break 
            if w > 0:
                result += 1
                rows[s[0]].remove(s)
                cols[s[1]].remove(s)
                for sr in rows[s[0]]:
                    heapq.heappush(heap, (len(rows[sr[0]])+len(cols[sr[1]])-2, (sr[0],sr[1])))
                for sc in cols[s[1]]:
                    heapq.heappush(heap, (len(rows[sc[0]])+len(cols[sc[1]])-2, (sc[0],sc[1])))
        return result
start_time = time.time()

t = Solution()
#root = t.removeDuplicateLetters("cbacdcbc")
root = t.removeStones([[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
