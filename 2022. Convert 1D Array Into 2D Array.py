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
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        return [[original[i*n+j] for j in range(n)] for i in range(m)]
start_time = time.time()

t = Solution()
#root = t.removeDuplicateLetters("cbacdcbc")
root = t.construct2DArray([1,2,3,4], 2, 2)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
