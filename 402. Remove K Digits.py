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
    # Definition for a binary tree node.
class Solution:    
    def removeKdigits(self, num: str, k: int) -> str:
        if len([c for c in num if c != '0']) <= k:
            return "0"
        i = 0
        while i < len(num)-1 and k > 0:
            if int(num[i]) > int(num[i+1]):            
                if i > 0:
                    num = num[:i] + num[i+1:]
                    i -= 1
                else: 
                    while num[i+1] == '0':
                        i += 1
                    num = num[i+1:]
                    i = 0
                k -= 1
            else: 
                i += 1
        if k > 0:
            num = num[:-k]
        return num
start_time = time.time()
t = Solution()
root = t.removeKdigits("11111111111222222222222222", 10)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
