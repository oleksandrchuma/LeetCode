import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import heapq
from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0 
        right = len(s)-1
        while left < right and s[left] == s[right]:
            c = s[left]
            while left < right and s[left] == c:
                left += 1
            while right > left and s[right] == c:
                right -= 1
            if left == right and s[left] == c:
                return 0 
        return right - left + 1
                  
        
start_time = time.time()
app = Solution()
root = app.minimumLength('aabccabba')

#root = app.calculateMinimumHP([[0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

