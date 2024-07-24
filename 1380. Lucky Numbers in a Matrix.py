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
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        lucky_row = [min(matrix[i]) for i in range(n)]
        lucky_col = [max([matrix[i][j] for i in range(n)]) for j in range(m)]
        return [matrix[i][j] for i in range(n) for j in range(m) 
                if  lucky_row[i] == lucky_col[j] and lucky_row[i] == matrix[i][j]]
start_time = time.time()
t = Solution()
#[5,1,2,3,null,6,4]
root = t.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]])

print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
