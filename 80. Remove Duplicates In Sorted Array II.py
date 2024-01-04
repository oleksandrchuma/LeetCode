from typing import List
from typing import Optional
import time
from collections import Counter
import math
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        read = 0; write = -1; curr = nums[0]; count = 0
        while read < len(nums):
            if (nums[read] == curr):
                count += 1
                if count <= 2:
                    write += 1
                    nums[write] = curr
            else:
                curr = nums[read]
                count = 1
                write += 1
                nums[write] = curr
            read+=1
        return write + 1
start_time = time.time()
print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3, 3, 3, 3, 4]))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

