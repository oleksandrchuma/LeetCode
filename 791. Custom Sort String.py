import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import itertools
import heapq
from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dict = {c:i for i,c in enumerate(order)}
        to_sort = [c for c in s if c in dict]
        to_sort.sort(key=lambda item: dict[item])
        result = ""
        pos = 0
        for i in range(len(s)):
            if s[i] in dict:
                result += to_sort[pos]
                pos += 1 
            else:
                result += s[i]
        return result
start_time = time.time()
t = Solution()
root = t.customSortString("bcafg", "abcd" )
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

