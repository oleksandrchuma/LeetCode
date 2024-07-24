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
    def pos(self, arr, x):
        if len(arr) == 0:
            return -1
        left = 0
        right = len(arr)-1
        while left < right:
            mid = (left + right)//2
            if arr[mid] > x and (mid == 0 or arr[mid-1] < x):
                return mid 
            if arr[mid] > x:
                right = mid-1
            else:
                left = mid+1
        if arr[left] < x:
            left += 1
        return left 
    def removeDuplicateLetters(self, s: str) -> str:
        letters = defaultdict(list)
        for i in range(len(s)):
            letters[s[i]].append(i)
        ordered = sorted(letters.keys())
        result = []
        while i < len(ordered):
            l = ordered[i]
            if len(result) == 0:
                result.append((l, letters[l][0]))
                i += 1
            else:
                for j in range(-1, len(result)):
                    if j == -1:
                        if result[0][0] > l and letters[l][0] < result[0][1]:
                            result.insert(0, (l, letters[l][0]))
                    else: 
                        if l > result[j][0] and (j == len(result)-1) or l < result[j+1][0]
                    
start_time = time.time()
t = Solution()
root = t.removeDuplicateLetters("thesqtitxyetpxloeevdeqifkz")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
