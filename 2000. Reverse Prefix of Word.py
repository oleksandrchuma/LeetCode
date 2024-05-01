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
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx != -1:
            word = ''.join(reversed(word[:idx+1]))+word[idx+1:]
        return word
start_time = time.time()
t = Solution()
root = t.reversePrefix("abc", "d")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
