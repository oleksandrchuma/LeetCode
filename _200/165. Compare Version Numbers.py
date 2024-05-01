import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import heapq 
class Solution:
    
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:    
        minus = (numerator<0) ^ (denominator<0)
        print(minus)
        numerator, denominator = abs(numerator), abs(denominator)
        intPart = numerator // denominator
        mod = numerator % denominator
        fractionParts = []
        fractionDic = {}
        while mod > 0 and mod not in fractionDic:
            exp = 0
            x = mod
            while x < denominator:
                x *= 10
                exp += 1
            part = str(x // denominator)
            fractionDic[mod] = len(fractionParts)
            fractionParts.append('0'*(exp-len(part)) + part)
            mod = x % denominator
        result = str(intPart)
        if len(fractionParts) > 0:
            if mod == 0:
                result += "." + "".join(fractionParts)
            else:
                result += "." + "".join(fractionParts[i] for i in range(fractionDic[mod]))
                result += "("+"".join(fractionParts[i] for i in range(fractionDic[mod],len(fractionParts)))+")"
        return ("-" if minus else "") + result
app = Solution()
start_time = time.time()
root = app.fractionToDecimal(-1, 2)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

