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
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = sorted(deck)
        index = 0
        n = len(deck)
        result = [0]*n
        skip = 0
        while index < n:
            for i in range(n):
                if result[i] == 0:
                    if skip == 1:
                        skip = 0
                    else:
                        result[i] = deck[index]
                        index += 1 
                        skip = 1
            
        return result  
start_time = time.time()
t = Solution()
root = t.deckRevealedIncreasing([17,13,11,2,3,5,7])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
