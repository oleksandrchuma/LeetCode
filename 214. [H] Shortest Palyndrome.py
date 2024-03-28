from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
 
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s 
        n = len(s)

        t = [0 for i in range(n//2+1)]
        for i in range(n//2+1):
            t[i] = s[n//2-i:].__hash__()
        oddtail = s
        tail = s
        x = ""
        for i in range(n//2+1):
            x = s[i] + x
            tail1 = x+s[(i+1)*2:] 
            if i < n//2 and tail1.__hash__() == t[-2-i] and len(tail1) < len(tail):
                tail = tail1
            tail2 = x+s[(i+1)*2-1:]
            if tail2.__hash__() == t[-i-1] in t:
                oddtail = tail2


        if len(oddtail)*2-1<len(tail)*2:
            return "".join(reversed(oddtail[1:]))+oddtail
           
        return "".join(reversed(tail))+tail
            
start_time = time.time()
app = Solution()
root = app.shortestPalindrome("aacecaaa")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


