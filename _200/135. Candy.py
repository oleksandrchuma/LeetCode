from typing import List
from typing import Optional
import time
import math
from functools import lru_cache 
from collections import Counter

class Solution:
    def candy(self, ratings: List[int]) -> int:
        levels = [0 for _ in ratings]        
        levels[0] = 1
        down=[]
        level = 1
        for i in range(1, len(ratings)):
            if ratings[i-1] > ratings[i]:
                if not(down):
                    down.append(i-1)
                down.append(i)
            else:
                k = 1
                while (down):
                    j = down.pop()
                    levels[j] = max(k, levels[j])
                    k += 1
                if ratings[i-1] == ratings[i]:
                    levels[i] = 1
                else:
                    levels[i] = levels[i-1]+1
        k = 1
        while (down):
            j = down.pop()
            levels[j] = max(k, levels[j])
            k += 1
        print(levels)
        return sum(levels)
start_time = time.time()
app = Solution()   
root = app.candy([1,2,2])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
