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

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        depth = int(math.ceil(math.log2(len(nums))))
        self.tree =[0]*(2*(2**depth))
        self.buildTree(0, len(nums)-1, 0)
        print(self.tree)

    def buildTree(self, left, right, index) -> int:
        if left == right:
            self.tree[index] = self.nums[left]
            return self.tree[index]
        mid = (left + right)//2
        self.tree[index] = self.buildTree(left, mid, 2*index+1)\
                          +self.buildTree(mid+1, right, 2*index+2)
        return self.tree[index]
    def update(self, index: int, val: int) -> None:
        delta = val-self.nums[index]
        self.updateVal(0, len(self.nums)-1, 0, index, delta)
        self.nums[index]=val
        return 
    
    def updateVal(self, left, right, t_index, index, delta):
        self.tree[t_index] += delta
        if left == right:
            return
        mid = (left+right)//2
        if index <= mid:
            self.updateVal(left, mid, 2*t_index+1, index, delta)
        else:
            self.updateVal(mid+1, right, 2*t_index+2, index, delta) 

    def sumRange(self, left: int, right: int) -> int:
        return self.getVal(left, right, 0, len(self.nums)-1, 0)
    
    def getVal(self, left, right, t_left, t_right, index) -> int:
        if t_right < left or t_left > right:
            return 0 
        if left <= t_left and t_right <= right:
            return self.tree[index]
        mid = (t_left+t_right)//2
        return self.getVal(left, right, t_left, mid,   2*index+1)\
              +self.getVal(left, right, mid+1,  t_right, 2*index+2)
    
start_time = time.time()
t = NumArray([7,2,7,2,0])
root = t.sumRange(2,4)
print(root)
t.update(2,4)
root = t.sumRange(2,4)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
