from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        m = max(c.values())
        return sum(v for k,v in c.items() if v == m)
app = Solution()
start_time = time.time()
root = app.maxFrequencyElements([1,2,3,4,5])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

