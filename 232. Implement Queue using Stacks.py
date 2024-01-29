from typing import List
from typing import Optional
import time
import math
from collections import Counter
class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)
        return 
    
    def pop(self) -> int:
        if not(self.output):
            while (self.input):
                self.output.append(self.input.pop())
        return self.output.pop()

    def peek(self) -> int:
        result = self.pop()
        self.output.append(result)
        return result

    def empty(self) -> bool:
        return not(self.input) and not(self.output)

start_time = time.time()
q = MyQueue()
q.push(1)
q.push(2)
print(q.pop())
print(q.peek())
q.push(3)
print(q.pop())
q.push(4)
print(q.pop())
print(q.pop())
print(q.empty())
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

