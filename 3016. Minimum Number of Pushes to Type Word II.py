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
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        i = 0
        result = 0
        for v in sorted(c.values(), reverse=True):
            result += v*(i//8+1)
            i+=1
        return result 
                            
start_time = time.time()
t = Solution()
#root = t.removeDuplicateLetters("cbacdcbc")
root = t.minimumPushes("aabbccddeeffgghhiiiiii")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
