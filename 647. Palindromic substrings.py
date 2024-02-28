from typing import List
from typing import Optional
import time
from collections import Counter
from functools import lru_cache 
class Solution:

    @lru_cache(None)
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                return False
        return True
    
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            for j in range(i+1):
                if (self.isPalindrome(s[j:i+1])):
                    result += 1
        return result 
    start_time = time.time()
app = Solution()   
start_time = time.time()
root = app.countSubstrings("aaa")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
