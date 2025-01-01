from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
import heapq
from collections import Counter
import pprint
import bisect

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def pos(arr, x):
            return bisect.bisect_left(arr, x)
        result = 0
        arr = []
        lessmore = []
        dic = {}
        n = len(rating)
        for i in range(len(rating)):
            p = pos(arr, rating[i])
            lessmore.append((p, len(arr)-p))
            dic[rating[i]] = i
            arr.insert(p, rating[i])
       # print(rating)
       # print(arr)
        for i in range(len(arr)):
            l1, m1 = lessmore[dic[arr[i]]]
            l2 = i - l1 
            m2 = n - l1 - m1 - l2 - 1
            result += l1*m2 + l2*m1

                    
        return result
         
    
start_time = time.time()
app = Solution()
root = app.numTeams([2,5,3,4,1])
#root = app.calculateMinimumHP([[0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

