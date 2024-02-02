from typing import List
from typing import Optional
import time
import math
import numpy
from collections import Counter
class Solution:
    def getNum(self, digits: List[int]) -> int:
        return int(''.join([str(d) for d in digits]))
    
    def getSequentialNumbers(self, k: int)->List[int]:
        digits = [i for i in range(1,10)]
        return [self.getNum(digits[i:i+k]) for i in range(10-k)]
    
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        if (low > high):
            return [] 
        kl = len(str(low))
        kh = len(str(high))
        result = []
        result = [
                    num
                    for k in range(kl, kh + 1)
                    for num in self.getSequentialNumbers(k)
                    if low <= num <= high
                ]
        return result                        
start_time = time.time()
app = Solution()

#root = app.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])
root = app.sequentialDigits(100, 300)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
