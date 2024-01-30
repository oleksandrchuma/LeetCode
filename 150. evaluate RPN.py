from typing import List
from typing import Optional
import time
import math
import numpy
from collections import Counter

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if (token in {"+", "*", "-", "/"}):
                y = int(stack.pop())
                x = int(stack.pop())
                if token == "+":
                    stack.append(x+y)
                elif token == "-":
                    stack.append(x-y)
                elif token == "*":
                    stack.append(x*y)
                elif token == "/":
                    m = abs(x)//abs(y)
                    sign = numpy.sign(x)*numpy.sign(y)
                    stack.append(sign*m)
            else: 
                stack.append(token)
        return stack.pop()
            
start_time = time.time()
app = Solution()
root = app.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
