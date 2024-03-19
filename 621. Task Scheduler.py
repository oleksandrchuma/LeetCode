from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        interval_count = max(counter.values())
        k = len([key for key,val in counter.items() if val == interval_count])
        gaps = max((n+1-k)*(interval_count-1), len(tasks)-(k*interval_count))

        return k*interval_count + gaps
            
start_time = time.time()
app = Solution()
root = app.leastInterval(["A","A","A", "B","B","B"], 3)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


