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
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        for i in range(1, len(chalk)):
            chalk[i] += chalk[i-1]
        k = k % chalk[-1]
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i 
        return -1
start_time = time.time()

t = Solution()
#root = t.removeDuplicateLetters("cbacdcbc")
root = t.chalkReplacer([3,4,1,2], 25)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
