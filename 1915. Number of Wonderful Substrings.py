from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
import heapq
class Solution:
    def bit_array_to_int(self, bit_array):
        result = 0
        for bit in bit_array:
            result = (result << 1) | bit
        return result
    def wonderfulSubstrings(self, word: str) -> int:
        k = 0
        d = defaultdict(int)
        result = 0
        d[0] = 1
        for c in word:
            bit = 1 << (ord(c)-ord('a'))
            k = k^bit
            result += d[k]
            for i in range(10):
                result += d[k^(1<<i)]
            d[k]+=1    
            print(bin(k))
        return result
start_time = time.time()
app = Solution()
root = app.wonderfulSubstrings("aabb")#aafjdceac
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


