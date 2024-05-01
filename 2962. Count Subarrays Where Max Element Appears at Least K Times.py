from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
 
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        
        max_elem = max(nums)
        max_pos = [i for i in range(len(nums)) if nums[i] == max_elem]
        deltas = []
        for i in range(len(max_pos)):
            if i == 0: 
                deltas.append(max_pos[i]+1)
            else:
                deltas.append(max_pos[i]-max_pos[i-1])
        deltas.append(len(nums)-max_pos[-1])
        print(max_pos)
        print(deltas)
        if len(max_pos) < k: 
            return 0
        result = 0
        s = sum([deltas[i] for i in range(k, len(deltas))])
        for i in range(len(deltas)-k):
            head = deltas[i]
            tail = s
            result += head*tail
            s -= deltas[i+k]
        return result 
start_time = time.time()
app = Solution()
root = app.countSubarrays([1,3,2,3,3], 2)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


