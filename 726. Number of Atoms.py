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
class Scaner: 
    def __init__(self, text: str) -> None:
        self.text = text
        self.pos = 0
    
    def read(self):
        if self.pos == len(self.text):
            return ("", 1)
        var_name = self.text[self.pos]
        if var_name == '(':
            self.pos += 1
            return (var_name, 1)
        i = 1
        while self.pos+i < len(self.text) and self.text[self.pos+i].islower():
            i += 1
        var_name = self.text[self.pos:self.pos+i]
        self.pos += i
        i = 0
        while self.pos+i < len(self.text) and self.text[self.pos+i].isdigit():
            i += 1
        str_num = self.text[self.pos:self.pos+i]
        num = 1
        if str_num != "":
            num = int(str_num)
        self.pos += i
        return (var_name, num)

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        s = Scaner(formula)
        level = 0
        result = defaultdict(int)
        stack = []
        while True:
            var_name, num = s.read()
            if var_name == "":
                break
            if var_name == "(":
                level += 1
                stack.append((var_name, level, 1))
            elif var_name == ")":
                if level == 1:
                    v = stack.pop()
                    while v[0] != '(':
                        result[v[0]] += v[2]*num
                        v = stack.pop()
                else: 
                    i = -1 
                    while stack[i][0] != '(':
                        v = stack[i]
                        stack[i] = v[0], v[1]-1, v[2]*num
                        i -= 1
                    stack.pop(i)
                level -= 1
            else:
                if level > 0: 
                    stack.append((var_name, level, num))
                else:
                    result[var_name] += num
        while stack:
            v = stack.pop()    
            result[v[0]] += v[2]
        return "".join((f"{e}{str(c)}" if c > 1 else e) for e, c in sorted(result.items()))
start_time = time.time()
t = Solution()
root = t.countOfAtoms("K4(ON(SO3)2)2")

print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
