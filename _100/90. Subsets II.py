from typing import List
from typing import Optional
import time
import math
from collections import Counter

class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '' or (s[0] == '0'):
            return 0
        rez = [0]*(len(s)+1)
        rez[0] = 1
        rez[1] = 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if int(s[i-1]) not in [1,2]: 
                    return 0
                rez[i+1] = rez[i-1]
            elif s[i-1] == '1' or (s[i-1]== '2' and int(s[i]) <= 6):
                rez[i+1] = rez[i-1] + rez[i]
            else: 
                rez[i+1] = rez[i]    
        return rez[len(s)]
                
start_time = time.time()
print(Solution().numDecodings("110"))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

