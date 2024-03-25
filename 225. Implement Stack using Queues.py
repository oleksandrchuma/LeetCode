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

class MyStack:
    def __init__(self):
        self.queue = Queue()
        self.top_elem = 0

    def push(self, x: int) -> None:
        self.queue.put(x)    
        self.top_elem = x

    def pop(self) -> int:
        size = self.queue.qsize()
        for i in range(size - 1):
            self.push(self.queue.get())

        return self.queue.get()

    def top(self) -> int:
        return self.top_elem if not(self.empty()) else -1

    def empty(self) -> bool:
        return self.queue.empty()
start_time = time.time()
t = MyStack()
t.push(1)
t.push(2)
t.push(3)
print(t.pop())
print(t.pop())
#root = t.calculate("(1+(4+5+2)-3)+(6+8)")
#print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''