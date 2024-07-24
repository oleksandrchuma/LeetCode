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
# Definition for singly-linked list.

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x >= y: 
            open = 'a'
            close = 'b' 
        else: 
            open = 'b'
            close = 'a'
            y,x = x,y
        i = 0
        n = len(s)
        res = 0
        while i < n:
            while i < n and s[i] not in ('a', 'b'):
                i += 1
            if i == n:
                break 
            start = i 
            while i < n and s[i] in ('a', 'b'):
                i += 1
            end = i
            word = list(s[start:end])
            while True:
                word, delta1 = self.calc(word, open, close)
                word, delta2 = self.calc(word, close, open)
                res += delta1*x + delta2*y
                if delta1 + delta2 == 0:
                    break
            
        return res
    def calc(self, word, open, close):
        stack = []
        res = 0
        count = 0
        for c in word:
            if c == open:
                count+=1
                stack.append(c)
            if c == close: 
                if count > 0:
                    count -= 1
                    stack.pop()
                    res += 1
                else:
                    stack.append(c)    
        return stack, res
start_time = time.time()
t = Solution()
root = t.maximumGain("aabbaaxybbaabb", 5, 4)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
