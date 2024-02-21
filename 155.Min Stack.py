import time
from typing import List
from functools import lru_cache

class MinStack:
    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        min = val if self.data or self.data[-1][1] > val else self.data[-1][1]
        self.data.append((val, min))

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]

#app = Solution()
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()        

start_time = time.time()
#root = app.isPowerOfTwo(2)
#root = app.mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]])
#print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

