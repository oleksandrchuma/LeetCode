from typing import List
from typing import Optional
import time
import math

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        maxlen = max(len(str(num)) for num in nums)
        
        s = "".join(sorted([str(num) for num in nums], 
                              key= lambda n: n*(2520//len(n)),
                              reverse=True))
        if (s.startswith('0')):
            return "0"
        return s
start_time = time.time()
app = Solution()
root = app.largestNumber([432,43243])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

 