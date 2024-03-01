from typing import List
from typing import Optional
import time
import math
from collections import Counter

class Node:
    val: int
    children: List[int]
    high: int 
    def __init__(self, low=0):
         self.low = low
         self.high = low
         self.children = []
    def print(self):
        print(f"{self.val} => {self.children}")
    def add(self, val):
        self.children.append(val)
    def get_val(self):
        return self.high-self.low
class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        low = prices[0]
        high = prices[0]
        start = prices[0]
        shorts = []
        deltas = []
        for i in range(1, len(prices)):
            if prices[i] < low:
                if (high - low > 0):
                    deltas.append(high - low)
                high = low = prices[i]
            if prices[i] > high: 
                high = prices[i]                  
            if prices[i] < prices[i-1]:
                if prices[i-1] - start > 0:
                    shorts.append(prices[i-1] - start)
                start = prices[i]
              
        if (high - low > 0):
            deltas.append(high - low)
        if prices[-1] - start > 0:
            shorts.append(prices[-1] - start)
                
        deltas.sort()
        shorts.sort()
        print(deltas)
        print(shorts)
        if len(deltas) > 2:
            return max(deltas[-1] + deltas[-2], shorts[-1] + shorts[-2])
        elif len(shorts) > 2: 
            return shorts[-1] + shorts[-2]
        else: 
            return sum(shorts)
        
    def maxProfit(self, prices: List[int]) -> int:
        prices = self.simplify(prices)
        if len(prices) <= 1: 
            return 0
        #print(prices)
        ml = prices[0]
        mh = prices[1]
        result = []
        result.append(mh-ml)
        for i in range(1, len(prices)//2):
            low = prices[i*2]
            high = prices[i*2+1]
            if low < ml: 
                ml = low
                mh = high
            elif high > mh: 
                mh = high
            if len(result) > 0:    
                result.append(max(mh-ml, result[-1]))
            else: 
                result.append(mh-ml)
        #print(result)
        ml = prices[-2]
        mh = prices[-1]
        i = len(prices)//2 - 1
        best = 0
        while i >= 1:
            low = prices[i*2]
            high = prices[i*2+1]
            if high > mh: 
                mh = high
                ml = low 
            elif low < ml: 
                ml = low
            best = max(mh-ml, best)
            result[i-1] += best 
            i -= 1
        return max(result)
    
    def simplify(self, prices: List[int])-> List[int]:
        if len(prices) <= 1:
            return prices 
        low = curr = prices[0]
        result = []
        for i in range(1, len(prices)):
            if prices[i] >= curr:
                curr = prices[i]
                continue
            if prices[i] < curr:
                if (curr > low):
                    result.append(low)
                    result.append(curr)
                low = curr = prices[i]
        if (curr > low):
            result.append(low)
            result.append(curr)
                    
        return result
    def matrix(self, prices):
        if len(prices) == 0:
            return []
        n = len(prices)//2
        res = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                low = prices[i*2]
                high = prices[j*2+1]
                res[i][j] = high-low
        return res
    
    def calc(self, matrix, k):
        n = len(matrix)
        res = [[0 for _ in range(n+1)] for _ in range(k+1)]
        for i in range(1, k+1):
            m = 0
            for j in range(1, n+1):
                for d in range(0, j):
                    m = max(m, matrix[n-j][n-j+d]+res[i-1][j-d-1])
                res[i][j] = m
            print(res[i])
        print(res)
start_time = time.time()
app = Solution()

#print(app.maxProfit([3,3,5,0,0,3,1,4]))
simp = app.simplify([3,3,5,0,0,3,1,4,0,5,1,8])
print(simp)
matrix = app.matrix(simp)
print(matrix)
app.calc(matrix, 3)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

