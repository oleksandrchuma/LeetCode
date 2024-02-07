from typing import List
from typing import Optional
import time
import math
from functools import lru_cache 
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        return (''.join(
                    ''.join([k]*v) 
                    for k, v in sorted(Counter(s).items(), 
                                       key=lambda item: item[1], 
                                       reverse=True)))
start_time = time.time()
app = Solution()   
root = app.frequencySort("Aatreae")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")