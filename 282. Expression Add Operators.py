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
class Solution:
    '''
        can rewrite using recursion 
        need just to track current value of expression and last operand of lower priority (last used with +/- operator)
        will be much better for memory consumption
        class Solution:
    def addOperators(self, s: str, target: int) -> List[str]:
        def backtrack(i, path, resultSoFar, prevNum):
            if i == len(s):
                if resultSoFar == target:
                    ans.append(path)
                return

            for j in range(i, len(s)):
                if j > i and s[i] == '0': break  # Skip leading zero number
                num = int(s[i:j + 1])
                if i == 0:
                    backtrack(j + 1, path + str(num), resultSoFar + num, num)  # First num, pick it without adding any operator
                else:
                    backtrack(j + 1, path + "+" + str(num), resultSoFar + num, num)
                    backtrack(j + 1, path + "-" + str(num), resultSoFar - num, -num)
                    backtrack(j + 1, path + "*" + str(num), resultSoFar - prevNum + prevNum * num, prevNum * num)  # Can imagine with example: 1+2*3*4

        ans = []
        backtrack(0, "", 0, 0)
        return ans
    '''
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        matr = [[defaultdict(list) for _ in range(n)] for _ in range(n)]
        for int_len in range(n):
            for i in range(n):
                if i + int_len >= n:
                    continue
                if num[i] != '0' or int_len == 0:
                    matr[i][i+int_len][int(num[i:(i+int_len+1)])].append([])
                for mul_pos in range(int_len):
                    if num[i+mul_pos+1] == '0' and mul_pos+1 < int_len:
                        continue

                    d1 = matr[i][i+mul_pos]
                    k2 = int(num[i+mul_pos+1:i+int_len+1])
                    #d2 = matr[i+mul_pos+1][i+int_len]
                    for k1, v1 in d1.items():
                        for vx1 in v1:
                            matr[i][i+int_len][k1*k2].append(vx1+[i+mul_pos])

        matr2 = [[defaultdict(list) for _ in range(n)] for _ in range(n)]
        for int_len in range(n):
            for i in range(n):
                if i + int_len >= n:
                    continue
                #if num[i] == '0' and int_len > 0:
                #    continue  
                matr2[i][i+int_len] = matr[i][i+int_len]
                for mul_pos in range(int_len):
                    d1 = matr2[i][i+mul_pos]
                    #k2 = int(num[i+mul_pos+1:i+int_len+1])
                    d2 = matr[i+mul_pos+1][i+int_len]
                    for k1, v1 in d1.items():
                        for k2, v2 in d2.items():
                            for vx1 in v1:
                                for vx2 in v2:
                                    if len(vx2) == 0 or max(vx2)<10:
                                        matr2[i][i+int_len][k1+k2].append(vx1+[i+mul_pos+10]+vx2)
                                        matr2[i][i+int_len][k1-k2].append(vx1+[i+mul_pos+20]+vx2)

        #print(matr[0][n-1])
        #print(matr2[0][n-1])
        result = []
        for ops in matr2[0][n-1][target]:
            left = 0
            func = []
            for operand in ops:
                if operand >= 20:
                    pos = operand - 20
                    op = '-'
                elif operand >= 10:
                    pos = operand - 10
                    op = '+'
                else:
                    pos = operand
                    op = '*'
                func.append(num[left:pos+1])
                func.append(op)
                left = pos+1
            func.append(num[left:])
            result.append(''.join(func))
        return list(set(result))

start_time = time.time()
t = Solution()
root = t.addOperators("3456237490", 9191)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
