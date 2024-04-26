from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
 
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = Counter(students)
        for s in sandwiches:
            if counter[s] > 0:
                counter[s] -= 1
            else: 
                return sum(counter.values())
        return 0
start_time = time.time()
app = Solution()
root = app.countStudents([1,1,1,0,0,1], [1,0,0,0,1,1])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


