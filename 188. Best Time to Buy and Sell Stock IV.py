from typing import List
from typing import Optional
import time
import math
from collections import Counter

class Solution:    
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
            #print(res[i])
        #print(res)
        return res
                
    def maxProfit(self, k: int, prices: List[int]) -> int:
        simp = self.simplify(prices)
        #print(simp)
        matrix = self.matrix(simp)
        #print(matrix)
        res = self.calc(matrix, k)
        return res[-1][-1]
    
start_time = time.time()
app = Solution()
print(app.maxProfit(2, [3,2,6,5,0,3]))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

