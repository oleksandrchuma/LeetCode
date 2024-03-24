import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import itertools
import heapq
from collections import Counter
class Scaner: 
    def __init__(self, s: str):
        self.s = s
        self.pos = 0
        self.n = len(s)
        self.priority = {
            '(':0, '+':2, '-':2,'*':3, '/':3, '~': 4, ')':1 
        }
    def scan(self):
        while self.pos < self.n and self.s[self.pos] == ' ':
            self.pos += 1
        if self.pos < self.n:
            if self.s[self.pos] in self.priority:
                self.pos += 1
                return self.s[self.pos-1], True
            num = ""
            while self.pos < self.n and self.s[self.pos].isdigit():
                num += self.s[self.pos]
                self.pos += 1
            return num, False
        return "", False
class Solution:
    def calculate(self, s: str) -> int:
        s = '('+s+')'
        scaner = Scaner(s) 
        lexem, is_oper = scaner.scan()
        prev_oper = "" 
        opers = []
        nums = []
        while lexem != "":
            if is_oper:
                if lexem == '-' and prev_oper != "":
                    lexem = '~'
                if lexem != "(":
                    while opers and scaner.priority[opers[-1]] >= scaner.priority[lexem]:
                        oper = opers.pop()
                        y = nums.pop()
                        if oper != '~':
                            x = nums.pop()
                        if oper == '+':
                            nums.append(x+y)
                        elif oper == '-':
                            nums.append(x-y)
                        elif oper == '/':
                            nums.append(x//y)
                        elif oper == '*':
                            nums.append(x*y)
                        elif oper == '~':
                            nums.append(-y)
                if lexem != ')':
                    opers.append(lexem)
                else:
                    opers.pop()
            else:
                nums.append(int(lexem))
            prev_oper = lexem if is_oper and lexem != ")" else ""
            lexem, is_oper = scaner.scan()
        return nums.pop() 
start_time = time.time()
t = Solution()
root = t.calculate("3/2")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''