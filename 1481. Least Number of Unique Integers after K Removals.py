import time
from typing import List
from collections import Counter
from functools import lru_cache

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if len(arr) == 0: 
            return 0
        x = sorted([(k,v) for (k,v) in Counter(arr).items()], key= lambda item: item[1])
        i = 0
        while i < len(x) and k >= x[i][1]:
            k -= x[i][1]
            i += 1
        return len(x) - i
        
start_time = time.time()
app = Solution()
root = app.findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

