import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
from queue import Queue
import math
import itertools
import heapq
from collections import Counter
    # Definition for a binary tree node.
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        repeats = []
        singles = []
        curr = nums[0]
        start = 0
        for i in range(1, len(nums)):
            if nums[i] != curr:
                singles.append(curr)
                repeats.append(i-start)
                curr = nums[i]
                start = i
        singles.append(curr)
        repeats.append(len(nums)-start)
        print(singles)
        print(repeats)  

        if k == 1:
            return sum((r*(r+1))//2 for r in repeats)
        n = len(singles)
        left = result = 0
        right = 0
        uniq = defaultdict(int)
        uniq[singles[0]] = 1
        distinct = 1
        while right < n:
            while right < n and distinct < k:
                right += 1
                if right < n:
                    uniq[singles[right]] += 1
                    if uniq[singles[right]] == 1:
                        distinct += 1
            if distinct == k: 
                tail = repeats[right]
                tailLen = 1
                while right + tailLen < n: 
                    if uniq[singles[right+tailLen]] == 0:
                        break
                    tail += repeats[right+tailLen]
                    tailLen += 1
                head = repeats[left]
                while left < right and distinct == k:
                    uniq[singles[left]] -= 1
                    if uniq[singles[left]] == 0:
                        left += 1
                        distinct -= 1
                        break
                    left += 1
                    head += repeats[left]
                 
                result += tail*head 
        return result 
        
start_time = time.time()
t = Solution()

#root = t.subarraysWithKDistinct([1,2,1,2,3], 2)
root = t.subarraysWithKDistinct([2,1,1,1,2], 1)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
