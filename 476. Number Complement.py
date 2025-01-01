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
    def findComplement(self, num: int) -> int:
        return int("".join("0" if c == "1" else "1" for c in bin(num)[2:]), 2)
start_time = time.time()

t = Solution()
#root = t.removeDuplicateLetters("cbacdcbc")
root = t.findComplement(5)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
