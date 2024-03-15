from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math

class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1:
            n = sum(pow(int(c), 2) for c in str(n))
            if n in s:
                return False
            s.add(n)
        return True
app = Solution()
start_time = time.time()
root = app.isHappy(19)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

