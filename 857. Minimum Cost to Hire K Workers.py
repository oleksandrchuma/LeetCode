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
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratio =sorted([((wage[i]/quality[i]), quality[i]) for i in range(len(wage))])
        heap = [-ratio[i][1] for i in range(k)]
        heapq.heapify(heap)
        sum_heap = -sum([s for s in heap])
        totals = []
        totals.append(sum_heap*ratio[k-1][0])

        for i in range(k, len(wage)):
            prev_qual = -heapq.heappop(heap)
            if (prev_qual > ratio[i][1]):
                sum_heap = sum_heap-prev_qual+ratio[i][1]
                total = sum_heap*ratio[i][0]
                totals.append(total)
                heapq.heappush(heap, -ratio[i][1]) 
            else:
                heapq.heappush(heap, -prev_qual)
        return min(totals)
start_time = time.time()
t = Solution()
root = t.mincostToHireWorkers([32,43,66,9,94,57,25,44,99,19], [187,366,117,363,121,494,348,382,385,262], 4)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
