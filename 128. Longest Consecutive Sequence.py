from typing import List
from typing import Optional
import time
from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dicStart = {}
        uniq = set()
        for num in nums:
            if num in uniq:
                continue
            uniq.add(num)
            if num + 1 in dicStart: 
                dicStart[num] = dicStart[num+1]
                del(dicStart[num+1])
            else: 
                dicStart[num] = num
        result = 0
        for num in list(dicStart.keys()):
            if num not in dicStart:
                continue
            while dicStart[num] + 1 in dicStart:
                next = dicStart[num] + 1
                dicStart[num] = dicStart[next]
                del(dicStart[next])
            result = max(result, dicStart[num] - num + 1)
        return result
start_time = time.time()
app = Solution()

root = app.longestConsecutive([])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
