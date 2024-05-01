from typing import List
from typing import Optional
import time
from functools import lru_cache 
from collections import Counter

class Solution:
    def minCut(self, s: str) -> int:
        @lru_cache(None)
        def isPalindrome(l, r):  # l, r inclusive
            if l >= r: return True
            if s[l] != s[r]: return False
            return isPalindrome(l+1, r-1)
        
        @lru_cache(None)
        def partition(s: str) -> int:    
            if len(s) == 0:
                return 0 
            result = [0 for _ in s]
            result[0] = 1
            for i in range(1, len(s)):
                if (isPalindrome(0, i)):
                    result[i] = 1
                else: 
                    #splits = []
                    minlen = i+2
                    for j in range(1, i+1):
                        if result[j-1] >= minlen-1:
                            continue
                        sub = s[j:i+1]
                        if (isPalindrome(j, i)):
                            result[i] = result[j-1] + 1
                            minlen = result[i]
                            if (minlen == 2):
                                break
                    #for split in splits:
                    #    if len(split) < len(result[i]):
                    #        result[i] = split
            
            return result[-1]
        
        return partition(s) - 1

start_time = time.time()
app = Solution()   

#root = app.minCut("aab")
root = app.minCut("aab")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
