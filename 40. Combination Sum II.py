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
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def comb(pos, target):
            result = []
            used = set()
            for i in range(pos, len(candidates)):
                if candidates[i] > target:
                    break
                if candidates[i] == target and candidates[i] not in used:
                    result.append([candidates[i]])
                    used.add(candidates[i])
                elif candidates[i] not in used:
                    used.add(candidates[i])
                    sub = comb(i+1, target-candidates[i])
                    for s in sub:
                        result.append([candidates[i]]+s)

            return result 
        candidates.sort()
        return comb(0, target)
    
             
start_time = time.time()

t = Solution()
#root = t.removeDuplicateLetters("cbacdcbc")
root = t.combinationSum2([2,5,2,1,2], 5)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
