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
        seg_count = 1 if len(nums) < 100 else (10 if len(nums) < 1000 else 100)   
        self.seg_length = len(nums) if seg_count == 1 else len(nums)//seg_count + 1
        self.segments = []

        for i in range(seg_count):
            l = self.seg_length if i < seg_count-1 else len(nums) - (seg_count-1)*self.seg_length
            self.segments.append([0 for _ in range(l)])
        self.nums = nums
        self.seg_updates = [True for _ in range(seg_count)]      

    def get_seg(self, index):
        if self.seg_updates[index]:
            s = 0
            seg_offset = index*self.seg_length
            for i in range(len(self.segments[index])):
                s += self.nums[seg_offset+i]
                self.segments[index][i] = s
            self.seg_updates[index] = False
        return self.segments[index]
    
    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        self.seg_updates[index//self.seg_length] = True

    def sumRange(self, left: int, right: int) -> int:
        start_seg = left//self.seg_length
        end_seg = right//self.seg_length
        res = 0
        for i in range(start_seg, end_seg+1):
            seg_index = -1 if i < end_seg else right%self.seg_length
            res += self.get_seg(i)[seg_index]
        left = left % self.seg_length
        if left > 0:
            res -= self.get_seg(start_seg)[left-1]
        return res

start_time = time.time()
t = NumArray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
root = t.sumRange(2,4)
print(root)
t.update(2,4)
root = t.sumRange(2,4)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
