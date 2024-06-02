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
#Below is the interface for Iterator, which is already defined for you.
class Iterator:
      
    def __init__(self, nums):
        self.nums = nums
        self.pos = 0
    def hasNext(self):
        return self.pos < len(self.nums)
    def next(self):
        self.pos = self.pos+1
        return self.nums[self.pos-1]

class PeekingIterator:  
    def __init__(self, iterator):
        self.iterator = iterator
        self.peek_val = None
    
    def peek(self):
        if self.peek_val is None:
            self.peek_val = self.next()
        return self.peek_val

    def next(self):
        if self.peek_val is not None:
            val = self.peek_val
            self.peek_val = None
            return val
        return self.iterator.next()
        

    def hasNext(self):
        return self.peek_val is not None or self.iterator.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
start_time = time.time()
#t = Solution()
l = [0,1,0,3,12]
#root = t.moveZeroes(l)
print(l)
#rint(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
