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
import numpy 
import pprint
import bisect 

class MedianFinder:
    def __init__(self):
        self.data = []        

    def addNum(self, num: int) -> None:
        bisect.insort(self.data, num)        

    def findMedian(self) -> float:
        n = len(self.data)
        if n == 0:
            return 0
        if n%2:
            return self.data[n//2]
        return sum(self.data[n//2-1:n//2+1])/2

medianFinder = MedianFinder()
medianFinder.addNum(1)    
medianFinder.addNum(2) 
print(medianFinder.findMedian())
medianFinder.addNum(3) 
print(medianFinder.findMedian())

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
start_time = time.time()
#t = Solution()
#root = t.removeNodes(ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8))))))
#t.print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
