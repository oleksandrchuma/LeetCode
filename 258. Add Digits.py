from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
 
class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num = sum(int(c) for c in str(num))
        return num
start_time = time.time()
app = Solution()
root = app.addDigits(38)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


